from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3

from ryu.app.wsgi import WSGIApplication, ControllerBase, route

from webob import Response
from json import dumps
import sys

from topologies.Configurations import configurations

from utils.Graph import host_mac_map, switch_dpid_map
# Imports look unused, but are dynamically used in the code, do not remove
from utils.Graph import graph_a, link_map_a
from utils.Graph import graph_b, link_map_b
from utils.Graph import graph_c, link_map_c

from utils.Pathfinding import find_shortest_path

NO_FLOWS = False
"""
If True, the controller will not install any flow.

This is used for debugging, as this way packets that would normally follow a flow
will be sent to the controller, generating a packetIn event that can be logged.

Otherwise the packets will generate such event once, and then follow the flow
"""

DEBUG = True
"""
If True, the controller will log all the packets that are received and the actions taken.
"""

REST_API_NAME = 'slicing_api_app'


class SlicingController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    # Expose WSGI to add REST API routes
    _CONTEXTS = {'wsgi': WSGIApplication}

    def __init__(self, *args, **kwargs):
        super(SlicingController, self).__init__(*args, **kwargs)
        self.configurations = None

        self.mac_to_port = {}

        self.hmm = host_mac_map
        self.sdm = switch_dpid_map
        self.graph = None
        self.link_map = None
        self.datapaths = {}
        self.routes = {}

        self.api = kwargs['wsgi']
        self.api.register(SlicingControllerRest, {REST_API_NAME: self})

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        dpid = datapath.id

        self.datapaths[str(dpid)] = datapath
        self.logger.info(f"Switch {dpid} connected")

        # Install table-miss flow entry
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]

        self.add_flow(datapath, 0, match, actions)

    def topology_init(self, topology):
        """
        Initialize the network topology based on the topology selected.
        """
        topology = topology.lower()
        self.configurations = configurations[topology]

        exec(f"self.graph = graph_{topology}")
        exec(f"self.link_map = link_map_{topology}")

        if not self.graph or not self.link_map:
            self.logger.error(f"Topology {topology} could not be initialized correctly")
            sys.exit(1)

    def default_configurator(self, configuration):
        """
        Default configuration for the controller. Note that any previously installed flow will be removed, this is intended to be run first.
        """
        # Clearing all flows from all switches
        self.remove_flows_from_switches(None)

        responses = [self.on_demand_add_flow(*rule) for rule in self.configurations[configuration]]
        errors = [r for r in responses if r['status'] != 200]
        if errors:
            self.logger.error(f"Errors occurred while installing configuration {configuration}")
            self.logger.error(errors)
            self.remove_flows_from_switches(None)
            return False

        self.logger.info("--------------------")
        self.logger.info(f"Configuration {configuration} installed successfully")
        self.logger.info("--------------------")
        return True

    def send_flow_stats_request(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        req = parser.OFPFlowStatsRequest(datapath, 0, ofproto.OFPTT_ALL)  # Request stats for all flows
        datapath.send_msg(req)

        self.logger.info(f"Flow stats request sent to switch {datapath.id}")

    def on_demand_add_flow(self, dpid, src_host, dst_host, port_in, port_out, priority, bandwidth, debug=True):
        """
        Extend the standard `add_flow` method to manually add a flow to a specific switch.
        """

        response = {'status': 404, 'message': f"Switch {self.sdm[dpid]} not found"}

        if dpid not in self.datapaths:
            return response

        next_hop = None
        for link in self.link_map[self.sdm[dpid]]:
            if self.link_map[self.sdm[dpid]][link][0] == port_out:
                next_hop = link
                break

        if self.link_map[self.sdm[dpid]][next_hop][1]['usage'] +  bandwidth < self.link_map[self.sdm[dpid]][next_hop][1]['capacity']:
            src_mac = self.hmm[src_host]
            dst_mac = self.hmm[dst_host]

            datapath = self.datapaths[dpid]
            parser = datapath.ofproto_parser
            match = parser.OFPMatch(in_port=port_in, eth_src=src_mac, eth_dst=dst_mac)
            actions = [parser.OFPActionOutput(port_out)]

            self.add_flow(datapath, priority, match, actions)

            response['status'] = 200
            response['message'] = f"Flow installed on switch {self.sdm[dpid]}: {match} -> {actions}"
        else:
            response['status'] = 401
            response['message'] = f"Link capacity exceeded on switch {self.sdm[dpid]}, port {port_out}"

        return response

    @staticmethod
    def add_flow(datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]

        mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match, instructions=inst)
        datapath.send_msg(mod)

    def add_route(self, src_host, dst_host, bandwidth):
        """
        Given source host, destination host and bandwidth, find the shortest path between the two that supports flows for the given bandwdith, then install them (if possible)
        :param src_host: source host name
        :param dst_host: destination host name
        :param bandwidth: bandwidth of the flows to be installed
        :return: response object with status and message
        """

        response = {'status': 404, 'message': f"No suitable path between {src_host} and {dst_host}"}
        path = find_shortest_path(self.graph, self.link_map, src_host, dst_host, bandwidth)

        if not path:
            return response

        self.logger.info(f"Path between {src_host} and {dst_host} found: {path}")
        if (src_host, dst_host) not in self.routes:
            flows = list()
            for i in range(1, (len(path) - 1)):
                in_port = self.link_map[path[i]][path[i - 1]][0]
                out_port = self.link_map[path[i]][path[i + 1]][0]
                flows.append((path[i], src_host, dst_host, in_port, out_port, bandwidth))
            self.routes[(src_host, dst_host)] = flows

            self.logger.info(f"Route between {src_host} and {dst_host} allocated, proceeding with installation")

            for flow in flows:
                # Install each flow
                src_mac = self.hmm[flow[1]]
                dst_mac = self.hmm[flow[2]]

                datapath = self.datapaths[self.sdm[flow[0]]]
                parser = datapath.ofproto_parser
                match = parser.OFPMatch(in_port=int(flow[3]), eth_src=src_mac, eth_dst=dst_mac)
                actions = [parser.OFPActionOutput(int(flow[4]))]

                self.add_flow(datapath, flow[5], match, actions)

                # Update usage map
                next_hop = None
                for link in self.link_map[flow[0]]:
                    if self.link_map[flow[0]][link][0] == flow[4]:
                        next_hop = link
                        break
                self.link_map[flow[0]][next_hop][1]['usage'] += flow[5]

                self.logger.info(f"Flow installed on switch {flow[0]}: {match} -> {actions}")

            response['status'] = 200
            response['message'] = f"Route between {src_host} and {dst_host} installed"
        else:
            response['status'] = 409
            response['message'] = f"Route between {src_host} and {dst_host} already exists"

        return response

    def remove_flow(self, dpid, src_host, dst_host, port_in, port_out, priority, bandwidth):
        response = {'status': 404, 'message': f'Datapath not found for switch {self.sdm[dpid]}'}  # Name of the switch

        datapath = self.datapaths.get(dpid, None)
        if datapath:
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser

            src_mac = self.hmm.get(src_host, None)
            dst_mac = self.hmm.get(dst_host, None)

            if not src_mac:
                self.logger.error(f"MAC address not found for source: {src_host}")
                response['message'] = f"MAC address not found for source: {src_host}"
                return response
            if not dst_mac:
                self.logger.error(f"MAC address not found for destination: {dst_host}")
                response['message'] = f"MAC address not found for destination: {dst_host}"
                return response

            match = parser.OFPMatch(in_port=port_in, eth_src=src_mac, eth_dst=dst_mac)

            flow_mod = parser.OFPFlowMod(
                datapath=datapath,
                command=ofproto.OFPFC_DELETE,
                match=match,
                out_port=port_out,  # Match any output port
                out_group=ofproto.OFPG_ANY,  # Match any group
                priority=priority,
            )

            datapath.send_msg(flow_mod)

            # Update link usage
            next_hop = None
            for link in self.link_map[self.sdm[dpid]]:
                if self.link_map[self.sdm[dpid]][link][0] == port_out:
                    next_hop = link
                    break
            self.link_map[self.sdm[dpid]][next_hop][1]['usage'] -= bandwidth

            response['status'] = 200
            response['message'] = f"Flow removed from switch {dpid}"

        return response

    def remove_flows_from_switches(self, dpids=None):
        """
        Removes all flows from the specified switches.

        Args: dpids (list or None): List of switch DPIDs to remove flows from. If None, removes flows from all switches.
        """
        target_dpids = dpids if dpids else self.datapaths.keys()

        for dpid in target_dpids:
            datapath = self.datapaths[dpid]
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser

            # Create a flow mod message to delete all flows
            flow_mod = parser.OFPFlowMod(
                datapath=datapath,
                command=ofproto.OFPFC_DELETE,  # Command to delete flows
                out_port=ofproto.OFPP_ANY,  # Apply to all ports
                out_group=ofproto.OFPG_ANY,  # Apply to all groups
                priority=0,  # Optional: match all priorities
                match=parser.OFPMatch()  # Match all flows
            )
            datapath.send_msg(flow_mod)
            switch_name = self.sdm[dpid]

            for neighbor in self.link_map[switch_name]:
                self.link_map[switch_name][neighbor][1]['usage'] = 0

            # self.logger.info(f"Removed all flows from switch {dpid}")

        self.logger.info("All flows removed from switches")

    @staticmethod
    def _send_package(msg, datapath, in_port, actions):
        data = None
        ofproto = datapath.ofproto
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = datapath.ofproto_parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=data,
        )
        datapath.send_msg(out)

    """
    Handler function for the FlowStatsReply event.
    Logs to the controller's console all the flows installed in a specified switch
    """

    @set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
    def _flow_stats_handler(self, ev):
        body = ev.msg.body

        self.logger.info(f"Flow stats received from switch {self.sdm[str(ev.msg.datapath.id)]}")
        for stat in body:
            self.logger.info(f"Flow: {stat.match} packets: {stat.packet_count} bytes: {stat.byte_count}")
        self.logger.info("--------------------")

    """
    Handler function for the PacketIn event (the controller receives a packet).
    It is to be noted that this function is not triggered when a packet is forwarded through an installed flow.
    """

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        pass
        # ========================
        # Old modified logic of self-learning switch, not needed for the slicing controller since it is based on manually installed flows
        # ========================

        # if ev.msg.msg_len < ev.msg.total_len:
        #     self.logger.debug("packet truncated: only %s of %s bytes",
        #                       ev.msg.msg_len, ev.msg.total_len)
        # msg = ev.msg
        # datapath = msg.datapath
        # ofproto = datapath.ofproto
        # parser = datapath.ofproto_parser
        # in_port = msg.match['in_port']
        #
        # pkt = packet.Packet(msg.data)
        # eth = pkt.get_protocols(ethernet.ethernet)[0]
        #
        # if eth.ethertype == ether_types.ETH_TYPE_LLDP:  # ignore lldp packet
        #     return
        #
        # dst = eth.dst
        # src = eth.src
        #
        # dpid = datapath.id
        #
        # if dpid in self.mac_to_port:
        #     if dst in self.mac_to_port[dpid]:
        #         out_port = self.mac_to_port[dpid][dst]
        #         actions = [parser.OFPActionOutput(out_port)]
        #         match = parser.OFPMatch(in_port=in_port, eth_dst=dst, eth_src=src)
        #
        #         if not NO_FLOWS: self.add_flow(datapath, 1, match, actions)
        #
        #         self._send_package(msg, datapath, in_port, actions)
        #         if DEBUG: self.logger.info(f"DESTINATION SWITCH REACHED | switch: {dpid} in_port: {in_port} {dst} out_port: {out_port}")
        #
        # elif dpid not in self.leaf_switches:
        #     out_port = ofproto.OFPP_FLOOD
        #     actions = [parser.OFPActionOutput(out_port)]
        #     match = parser.OFPMatch(in_port=in_port)
        #
        #     # These flows are always installed when starting the network, as they rely on flooding packets
        #     # By doing this, we can also log the packets just the first (and only) time they are flooded
        #     self.add_flow(datapath, 1, match, actions)
        #     self._send_package(msg, datapath, in_port, actions)
        #     if DEBUG: self.logger.info(f"Packet received | switch: {datapath.id} in_port {in_port} - FLOOD")


class SlicingControllerRest(ControllerBase):
    """
    This class defines the exposed REST API endpoint for the controller. It is to be noted that they all take a <dpid> as the id of the switch, but the actual command
    connected to each endpoint takes in the name of the switch (e.g. s1, s2, s3, ...). Additionally, the hosts are also taken by their names (e.g. h1, h2, h3, ...),
    the conversion to MAC addresses, if necessary, is handled in the function body.

    The endpoints are defined as follows:

    - Add a flow:
    Manually add a flow to a specific switch (note that every flow is only one-directional).
    /add_flow/{dpid}/{src_host}/{dst_host}/{port_in}/{port_out}/{priority}/{bandwidth}
    :param dpid: str
    :param src_host: str
    :param dst_host: str
    :param port_in: int
    :param port_out: int
    :param priority: int
    :param bandwidth: int

    :return: 200 if the flow was successfully installed
    :return: 404 if the switch was not found
    :return: 401 if there is not enough capacity on the link
    :return: 500 if there was an error

    - Remove a flow:
    Manually remove a flow from a specific switch. Takes the exact arguments as the add_flow
    /remove_flow/{dpid}/{src_host}/{dst_host}/{port_in}/{port_out}/{priority}/{bandwidth}/{bid}
    :param dpid: str
    :param src_host: str
    :param dst_host: str
    :param port_in: int
    :param port_out: int
    :param priority: int
    :param bandwidth: int
    :param bid: str ('t' or 'f')

    :return: 200 if the flow was successfully removed
    :return: 404 if the switch was not found
    :return: 500 if there was an error

    - Show flows:
    Request the flow stats from a specific switch. The flow list is only visible on the controller's console.
    /flows/{dpid}
    :param dpid: str

    :return: 200 if the flow stats request was successfully sent
    :return: 404 if the switch was not found

    - Default configurator:
    Install a default configuration on the network for simplified and more efficient testing.
    /default_configurator/{configuration}
    :param configuration: int

    :return: 200 if the configuration was successfully applied
    :return: 400 if the configuration is invalid
    """

    def __init__(self, req, link, data, **config):
        super(SlicingControllerRest, self).__init__(req, link, data, **config)
        self.slicing_app = data[REST_API_NAME]

    @route('slicing', '/topo_init/{topo}', methods=['GET'])
    def _topo_init(self, req, **kwargs):
        topo = kwargs['topo']
        self.slicing_app.topology_init(topo)
        return Response(status=200, body=dumps({"message": f"Topology {topo} initialized"}))

    @route('slicing', '/default_configurator/{configuration}', methods=['GET'])
    def _default_configurator(self, req, **kwargs):
        configuration = int(kwargs['configuration'])
        if configuration not in self.slicing_app.configurations.keys():
            available_configurations = [i for i in self.slicing_app.configurations.keys()]
            return Response(status=400, body=dumps({"message": f"Invalid configuration number, try: {', '.join(map(str, available_configurations))}"}))

        res = self.slicing_app.default_configurator(configuration)
        if not res:
            return Response(status=500, body=dumps({"message": f"Failed to apply configuration {configuration}"}))

        return Response(status=200, body=dumps({"message": f"Configuration {configuration} applied"}))

    @route('slicing', '/flows/{switch_name}', methods=['GET'])
    def _show_flows(self, req, **kwargs):
        switch_name = kwargs['switch_name']
        dpid = self.slicing_app.sdm.get(switch_name, None)
        dp = self.slicing_app.datapaths.get(dpid, None)

        if not dpid or not dp:
            return Response(status=404, body=dumps({"message": f"Switch {switch_name} not found"}))

        self.slicing_app.send_flow_stats_request(dp)
        return Response(status=200, body=dumps({"message": f"Flow stats request sent to switch {switch_name}"}))

    @route('slicing', '/add_flow/{switch_name}/{src_host}/{dst_host}/{port_in}/{port_out}/{priority}/{bandwidth}', methods=['GET'])
    def _add_flow(self, req, **kwargs):
        switch_name = kwargs['switch_name']
        src_host = kwargs['src_host']
        dst_host = kwargs['dst_host']
        port_in = int(kwargs['port_in'])
        port_out = int(kwargs['port_out'])
        priority = int(kwargs['priority'])
        bandwidth = int(kwargs['bandwidth'])

        dpid = self.slicing_app.sdm.get(switch_name, None)
        if not dpid:
            return Response(status=404, body=dumps({"message": f"Switch {switch_name} not found"}))

        result = self.slicing_app.on_demand_add_flow(dpid, src_host, dst_host, port_in, port_out, priority, bandwidth)
        return Response(status=result['status'], body=dumps({"message": result['message']}))

    @route('slicing', '/add_route/{src_host}/{dst_host}/{bandwidth}', methods=['GET'])
    def _add_route(self, req, **kwargs):
        src_host = kwargs['src_host']
        dst_host = kwargs['dst_host']
        bandwidth = int(kwargs['bandwidth'])

        result = self.slicing_app.add_route(src_host, dst_host, bandwidth)
        return Response(status=result['status'], body=dumps({"message": result['message']}))

    @route('slicing', '/remove_flow/{switch_name}/{src_host}/{dst_host}/{port_in}/{port_out}/{priority}/{bandwidth}', methods=['GET'])
    def _remove_flow(self, req, **kwargs):
        switch_name = kwargs['switch_name']
        src_host = kwargs['src_host']
        dst_host = kwargs['dst_host']
        port_in = int(kwargs['port_in'])
        port_out = int(kwargs['port_out'])
        priority = int(kwargs['priority'])
        bandwidth = int(kwargs['bandwidth'])

        dpid = self.slicing_app.sdm.get(switch_name, None)
        if not dpid:
            return Response(status=404, body=dumps({"message": f"Switch {switch_name} not found"}))

        result = self.slicing_app.remove_flow(dpid, src_host, dst_host, port_in, port_out, priority, bandwidth)
        return Response(status=result['status'], body=dumps({"message": result['message']}))

    @route('slicing', '/clear_switch/{switch_name}', methods=['GET'])
    def _clear_switch(self, req, **kwargs):
        switch_name = kwargs['switch_name']
        dpid = self.slicing_app.sdm.get(switch_name, None)
        dp = self.slicing_app.datapaths.get(dpid, None)

        if not dpid or not dp:
            return Response(status=404, body=dumps({"message": f"Switch {self.slicing_app.sdm[dpid]} not found"}))

        self.slicing_app.remove_flows_from_switches([dpid])
        return Response(status=200, body=dumps({"message": f"Switch {self.slicing_app.sdm[dpid]} cleared"}))
