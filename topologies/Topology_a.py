from mininet.topo import Topo


class TopologyA(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Templates for the different links, based on slices
        link_config_a = dict(bw=5)
        link_config_b = dict(bw=7)
        link_config_c = dict(bw=10)
        link_config_d = dict(bw=20)
        link_config_z = dict()

        # Create 9 switch nodes
        self.addSwitch("s1", dpid="0000000000000001")
        self.addSwitch("s2", dpid="0000000000000002")
        self.addSwitch("s3", dpid="0000000000000003")
        self.addSwitch("s4", dpid="0000000000000004")

        # Create 5 host nodes
        self.addHost("h1", inNamespace=True, mac="00:00:00:00:00:01")
        self.addHost("h2", inNamespace=True, mac="00:00:00:00:00:02")
        self.addHost("h3", inNamespace=True, mac="00:00:00:00:00:03")
        self.addHost("h4", inNamespace=True, mac="00:00:00:00:00:04")

        # Add switch links
        self.addLink("s1", "s2", **link_config_a)
        self.addLink("s1", "s3", **link_config_d)
        self.addLink("s1", "s4", **link_config_b)
        self.addLink("s2", "s3", **link_config_c)
        self.addLink("s2", "s4", **link_config_c)
        self.addLink("s3", "s4", **link_config_a)

        # Add host links
        self.addLink("h1", "s1", **link_config_z)
        self.addLink("h2", "s2", **link_config_z)
        self.addLink("h3", "s3", **link_config_z)
        self.addLink("h4", "s4", **link_config_z)



