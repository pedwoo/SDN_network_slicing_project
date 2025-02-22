from mininet.cli import CLI
import requests

from webob import Response
from json import dumps


class ExtendedCLI(CLI):
    def __init__(self, mininet, *args, **kwargs):
        super().__init__(mininet, *args, **kwargs)

    @staticmethod
    def do_addroute(line):
        args = line.split()
        if len(args) != 3:
            print("Usage: addroute <src_host_name> <dst_host_name> <bandwidth>")
            return

        try:
            url = f"http://localhost:8080/add_route/{args[0]}/{args[1]}/{int(args[2])}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'message': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")

    @staticmethod
    def do_addflow(line):
        """
        Install a flow on a switch.
        Usage: addflow <switch_name> <src_host_name> <dst_host_name> <port_1 (src -> dst)> <port_2 (dst -> src)> <priority> <bandwidth>
        Example: addflow s1 h1 h2 4 1 100 5 (4 is the port in s1 that goes to h1, 1 is the port in s1 that goes to the switch of h2)
        """
        args = line.split()
        if len(args) != 7:
            print("Usage: addflow <switch_name> <src_host_name> <dst_host_name> <port_1 (src -> dst)> <port_2 (dst -> src)> <priority> <bandwidth>")
            return

        try:
            """
            Parameters in order: 
            - dpid (switch identifier)
            - source_host (name)
            - destination_host (name)
            - port_1 (src -> dst)
            - port_2 (dst -> src)
            - priority (int)
            - bandwidth (int)
            """
            url = f"http://localhost:8080/add_flow/{args[0]}/{args[1]}/{args[2]}/{int(args[3])}/{int(args[4])}/{int(args[5])}/{int(args[6])}"

            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'message': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")

    @staticmethod
    def do_flows(line):
        args = line.split()
        if len(args) != 1:
            print("Usage: flows <switch_name>")
            return

        try:
            url = f"http://localhost:8080/flows/{args[0]}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=999, body=dumps({'response': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'response': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")

    @staticmethod
    def do_remflow(line):
        args = line.split()
        if len(args) != 7:
            print("Usage: remflow <switch_name> <src_host_name> <dst_host_name> <port_in> <port_out> <priority> <bandwidth>")
            return

        try:
            url = f"http://localhost:8080/remove_flow/{args[0]}/{args[1]}/{args[2]}/{int(args[3])}/{int(args[4])}/{int(args[5])}/{int(args[6])}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'response': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")

    @staticmethod
    def do_clrsw(line):
        args = line.split()
        if len(args) != 1:
            print("Usage: clrsw <switch_name>")
            return

        try:
            url = f"http://localhost:8080/clear_switch/{args[0]}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'response': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")

    @staticmethod
    def do_config(line):
        args = line.split()
        if len(args) != 1:
            print("Usage: config <config>")
            return

        config = args[0]

        try:
            url = f"http://localhost:8080/default_configurator/{config}"
            response = requests.get(url)

        except requests.exceptions.RequestException as e:
            response = Response(status=404, body=dumps({'message': f"Failed to contact RYU controller: {e}"}))
        except Exception as e:
            response = Response(status=500, body=dumps({'response': f"Unexpected error: {e}"}))

        print(f"STATUS: {response.status_code} | {response.json()['message']}")
