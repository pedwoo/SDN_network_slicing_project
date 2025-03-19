import time

from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.link import TCLink

import sys
from webob import Response
from json import dumps
import requests

from utils.ExtendedCLI import ExtendedCLI

from topologies.Configurations import configurations

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 Client.py <topology: {', '.join(configurations.keys())}>")
        sys.exit(1)

    topology_name = sys.argv[1].lower()
    if topology_name not in configurations.keys():
        print(f"Topology [{topology_name}] not found")
        sys.exit(1)
    else:
        print(f"Topology selected: [{topology_name}]")

    # Dynamically select the topology
    topo = None
    exec(f"from topologies.Topology_{topology_name.lower()} import Topology{topology_name.upper()}")
    exec(f"topo = Topology{topology_name.upper()}()")

    if topo:
        net = Mininet(
            topo=topo,
            switch=OVSKernelSwitch,
            build=False,
            autoSetMacs=True,
            autoStaticArp=True,
            link=TCLink,
        )
        controller = RemoteController("c0", ip="127.0.0.1", port=6653)
        net.addController(controller)

        net.build()
        print("Topology created. Press Enter to continue")
        input()

        try:
            url = f"http://localhost:8080/topo_init/{topology_name}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'response': f"Unexpected error: {e}"}))

        if response.status_code != 200:
            print(f"Failed to initialize topology [{topology_name}], error: {response}")
            sys.exit(0)

        net.start()

        # ========================
        # Testing script
        # ========================

        if topology_name == 'b':

            # Requests are done without try except as they are not expected to fail
            # Instal flows between h2 and h1 12Mbps both ways
            requests.get("http://localhost:8080/add_route/h1/h2/12")
            requests.get("http://localhost:8080/add_route/h2/h1/12")

            # Install flows between h2 and h3 7Mbps both ways
            requests.get("http://localhost:8080/add_route/h2/h3/7")
            requests.get("http://localhost:8080/add_route/h3/h2/7")

            # Install flows between h2 and h5 1Mbps both ways
            requests.get("http://localhost:8080/add_route/h2/h5/1")
            requests.get("http://localhost:8080/add_route/h5/h2/1")

            time.sleep(5)
            # Get the hosts
            server = net.get("h2") # h2 is the receiver
            h1 = net.get("h1")
            h3 = net.get("h3")
            h5 = net.get("h5")

            # Start the server
            server.cmd('iperf -s -u -p 1001 > ./test_stats/server_a.txt &')
            server.cmd('iperf -s -u -p 1002 > ./test_stats/server_b.txt &')
            server.cmd('iperf -s -u -p 1003 > ./test_stats/server_c.txt &')
            print("iperf server started on h2")

            h1.cmd('iperf -c 10.0.0.2 -u -t 20 -i 1 -b 12m -p 1001 > ./test_stats/h1_stats.txt &')
            h3.cmd('iperf -c 10.0.0.2 -u -t 20 -i 1 -b 7m -p 1002 > ./test_stats/h3_stats.txt &')
            h5.cmd('iperf -c 10.0.0.2 -u -t 20 -i 1 -b 1m -p 1003 > ./test_stats/h5_stats.txt &')

            print("iperf client executed")

        ExtendedCLI(net)
        net.stop()
    else:
        print(f"Failed to create topology [{topology_name}]")
        sys.exit(0)
