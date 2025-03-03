from mininet.topo import Topo


class TopologyB(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Templates for the different links, based on slices
        link_config_a = dict(bw=0.005)
        link_config_b = dict(bw=0.007)
        link_config_c = dict(bw=0.01)
        link_config_d = dict(bw=0.02)
        link_config_z = dict()

        # Create 9 switch nodes
        self.addSwitch("s1", dpid="0000000000000001")
        self.addSwitch("s2", dpid="0000000000000002")
        self.addSwitch("s3", dpid="0000000000000003")
        self.addSwitch("s4", dpid="0000000000000004")
        self.addSwitch("s5", dpid="0000000000000005")
        self.addSwitch("s6", dpid="0000000000000006")
        self.addSwitch("s7", dpid="0000000000000007")
        self.addSwitch("s8", dpid="0000000000000008")
        self.addSwitch("s9", dpid="0000000000000009")

        # Create 5 host nodes
        self.addHost("h1", inNamespace=True, mac="00:00:00:00:00:01")
        self.addHost("h2", inNamespace=True, mac="00:00:00:00:00:02")
        self.addHost("h3", inNamespace=True, mac="00:00:00:00:00:03")
        self.addHost("h4", inNamespace=True, mac="00:00:00:00:00:04")
        self.addHost("h5", inNamespace=True, mac="00:00:00:00:00:05")

        # Add switch links
        self.addLink("s1", "s2", **link_config_d)
        self.addLink("s1", "s6", **link_config_b)
        self.addLink("s1", "s9", **link_config_a)
        self.addLink("s2", "s3", **link_config_a)
        self.addLink("s2", "s4", **link_config_d)
        self.addLink("s3", "s5", **link_config_a)
        self.addLink("s4", "s5", **link_config_d)
        self.addLink("s6", "s7", **link_config_a)
        self.addLink("s6", "s8", **link_config_c)
        self.addLink("s7", "s9", **link_config_a)
        self.addLink("s8", "s9", **link_config_c)

        # Add host links
        self.addLink("h1", "s1", **link_config_z)
        self.addLink("h2", "s5", **link_config_z)
        self.addLink("h3", "s2", **link_config_z)
        self.addLink("h4", "s6", **link_config_z)
        self.addLink("h5", "s9", **link_config_z)



