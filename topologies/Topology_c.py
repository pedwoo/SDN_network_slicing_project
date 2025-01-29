from mininet.topo import Topo


class TopologyC(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Templates for the different links, based on slices
        link_config_a = dict(bw=5)
        link_config_b = dict(bw=7)
        link_config_c = dict(bw=10)
        link_config_d = dict(bw=20)
        link_config_z = dict()

        # Create 12 switch nodes
        self.addSwitch("s1", dpid="0000000000000001")
        self.addSwitch("s2", dpid="0000000000000002")
        self.addSwitch("s3", dpid="0000000000000003")
        self.addSwitch("s4", dpid="0000000000000004")
        self.addSwitch("s5", dpid="0000000000000005")
        self.addSwitch("s6", dpid="0000000000000006")
        self.addSwitch("s7", dpid="0000000000000007")
        self.addSwitch("s8", dpid="0000000000000008")
        self.addSwitch("s9", dpid="0000000000000009")
        self.addSwitch("s10", dpid="000000000000000A")
        self.addSwitch("s11", dpid="000000000000000B")
        self.addSwitch("s12", dpid="000000000000000C")

        # Create 7 host nodes
        self.addHost("h1", inNamespace=True, mac="00:00:00:00:00:01")
        self.addHost("h2", inNamespace=True, mac="00:00:00:00:00:02")
        self.addHost("h3", inNamespace=True, mac="00:00:00:00:00:03")
        self.addHost("h4", inNamespace=True, mac="00:00:00:00:00:04")
        self.addHost("h5", inNamespace=True, mac="00:00:00:00:00:05")
        self.addHost("h6", inNamespace=True, mac="00:00:00:00:00:06")
        self.addHost("h7", inNamespace=True, mac="00:00:00:00:00:07")

        # Add switch links
        self.addLink("s1", "s2", **link_config_b)
        self.addLink("s1", "s10", **link_config_b)
        self.addLink("s2", "s3", **link_config_a)
        self.addLink("s2", "s11", **link_config_c)
        self.addLink("s3", "s11", **link_config_c)
        self.addLink("s4", "s5", **link_config_b)
        self.addLink("s4", "s11", **link_config_a)
        self.addLink("s5", "s8", **link_config_c)
        self.addLink("s6", "s8", **link_config_a)
        self.addLink("s6", "s12", **link_config_a)
        self.addLink("s7", "s10", **link_config_a)
        self.addLink("s7", "s12", **link_config_a)
        self.addLink("s8", "s9", **link_config_d)
        self.addLink("s9", "s10", **link_config_d)
        self.addLink("s9", "s11", **link_config_b)
        self.addLink("s10", "s11", **link_config_a)
        self.addLink("s10", "s12", **link_config_c)

        # Add host links
        self.addLink("h1", "s1", **link_config_z)
        self.addLink("h2", "s2", **link_config_z)
        self.addLink("h3", "s3", **link_config_z)
        self.addLink("h4", "s4", **link_config_z)
        self.addLink("h5", "s5", **link_config_z)
        self.addLink("h6", "s6", **link_config_z)
        self.addLink("h7", "s7", **link_config_z)