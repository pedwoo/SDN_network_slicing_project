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
        ExtendedCLI(net)
        net.stop()
    else:
        print(f"Failed to create topology [{topology_name}]")
        sys.exit(0)
