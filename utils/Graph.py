link_a = 5
link_b = 7
link_c = 10
link_d = 20
link_z = 424242  # Arbitrary high value

# ==========
# Topology A
# ==========
leaf_switches_a = [1, 2, 3, 4]

# Bidirectional dictionary of the hosts in the topology
host_mac_map_a = {
    'h1': '00:00:00:00:00:01',
    'h2': '00:00:00:00:00:02',
    'h3': '00:00:00:00:00:03',
    'h4': '00:00:00:00:00:04',
    '00:00:00:00:00:01': 'h1',
    '00:00:00:00:00:02': 'h2',
    '00:00:00:00:00:03': 'h3',
    '00:00:00:00:00:04': 'h4'
}

# Bidirectional dictionary of the switches in the topology
switch_dpid_map_a = {
    's1': '1', '1': 's1',
    's2': '2', '2': 's2',
    's3': '3', '3': 's3',
    's4': '4', '4': 's4'
}

# Bidirectional dictionary of the links in the topology A
links_map_a = dict()

links_map_a[('1', '1')] = links_map_a[('2', '1')] = {'capacity': link_a, 'usage': 0}
links_map_a[('1', '2')] = links_map_a[('3', '1')] = {'capacity': link_d, 'usage': 0}
links_map_a[('1', '3')] = links_map_a[('4', '1')] = {'capacity': link_b, 'usage': 0}
links_map_a[('2', '2')] = links_map_a[('3', '2')] = {'capacity': link_c, 'usage': 0}
links_map_a[('2', '3')] = links_map_a[('4', '2')] = {'capacity': link_c, 'usage': 0}
links_map_a[('3', '3')] = links_map_a[('4', '3')] = {'capacity': link_a, 'usage': 0}

links_map_a[('1', '4')] = {'capacity': link_z}
links_map_a[('2', '4')] = {'capacity': link_z}
links_map_a[('3', '4')] = {'capacity': link_z}
links_map_a[('4', '4')] = {'capacity': link_z}

# ==========
# Topology B
# ==========
leaf_switches_b = [1, 2, 5, 6, 9]

# Bidirectional dictionary of the hosts in the topology
host_mac_map_b = {
    'h1': '00:00:00:00:00:01',
    'h2': '00:00:00:00:00:02',
    'h3': '00:00:00:00:00:03',
    'h4': '00:00:00:00:00:04',
    'h5': '00:00:00:00:00:05',
    '00:00:00:00:00:01': 'h1',
    '00:00:00:00:00:02': 'h2',
    '00:00:00:00:00:03': 'h3',
    '00:00:00:00:00:04': 'h4',
    '00:00:00:00:00:05': 'h5'
}

# Bidirectional dictionary of the switches in the topology
switch_dpid_map_b = {
    's1': '1', '1': 's1',
    's2': '2', '2': 's2',
    's3': '3', '3': 's3',
    's4': '4', '4': 's4',
    's5': '5', '5': 's5',
    's6': '6', '6': 's6',
    's7': '7', '7': 's7',
    's8': '8', '8': 's8',
    's9': '9', '9': 's9'
}

# Bidirectional dictionary of the links in the topology B
links_map_b = dict()

links_map_b[('1', '1')] = links_map_b[('2', '1')] = {'capacity': link_d, 'usage': 0}
links_map_b[('1', '2')] = links_map_b[('6', '3')] = {'capacity': link_b, 'usage': 0}
links_map_b[('1', '3')] = links_map_b[('9', '3')] = {'capacity': link_a, 'usage': 0}
links_map_b[('2', '2')] = links_map_b[('3', '1')] = {'capacity': link_a, 'usage': 0}
links_map_b[('2', '3')] = links_map_b[('4', '1')] = {'capacity': link_d, 'usage': 0}
links_map_b[('3', '2')] = links_map_b[('5', '1')] = {'capacity': link_a, 'usage': 0}
links_map_b[('4', '2')] = links_map_b[('5', '2')] = {'capacity': link_d, 'usage': 0}
links_map_b[('6', '1')] = links_map_b[('7', '1')] = {'capacity': link_a, 'usage': 0}
links_map_b[('6', '2')] = links_map_b[('8', '1')] = {'capacity': link_c, 'usage': 0}
links_map_b[('7', '2')] = links_map_b[('9', '1')] = {'capacity': link_a, 'usage': 0}
links_map_b[('8', '2')] = links_map_b[('9', '2')] = {'capacity': link_c, 'usage': 0}

links_map_b[('1', '4')] = {'capacity': link_z}
links_map_b[('2', '4')] = {'capacity': link_z}
links_map_b[('5', '3')] = {'capacity': link_z}
links_map_b[('6', '4')] = {'capacity': link_z}
links_map_b[('9', '4')] = {'capacity': link_z}

# ==========
# Topology C
# ==========
leaf_switches_c = [1, 2, 3, 4, 5, 6, 7]

# Bidirectional dictionary of the hosts in the topology
host_mac_map_c = {
    'h1': '00:00:00:00:00:01',
    'h2': '00:00:00:00:00:02',
    'h3': '00:00:00:00:00:03',
    'h4': '00:00:00:00:00:04',
    'h5': '00:00:00:00:00:05',
    'h6': '00:00:00:00:00:06',
    'h7': '00:00:00:00:00:07',
    '00:00:00:00:00:01': 'h1',
    '00:00:00:00:00:02': 'h2',
    '00:00:00:00:00:03': 'h3',
    '00:00:00:00:00:04': 'h4',
    '00:00:00:00:00:05': 'h5',
    '00:00:00:00:00:06': 'h6',
    '00:00:00:00:00:07': 'h7'
}

# Bidirectional dictionary of the switches in the topology
switch_dpid_map_c = {
    's1': '1', '1': 's1',
    's2': '2', '2': 's2',
    's3': '3', '3': 's3',
    's4': '4', '4': 's4',
    's5': '5', '5': 's5',
    's6': '6', '6': 's6',
    's7': '7', '7': 's7',
    's8': '8', '8': 's8',
    's9': '9', '9': 's9',
    's10': '10', '10': 's10',
    's11': '11', '11': 's11',
    's12': '12', '12': 's12'
}

# Bidirectional dictionary of the links in the topology C
links_map_c = dict()

links_map_c[('1', '1')] = links_map_c[('2', '1')] = {'capacity': link_b, 'usage': 0}
links_map_c[('1', '2')] = links_map_c[('10', '1')] = {'capacity': link_b, 'usage': 0}
links_map_c[('2', '2')] = links_map_c[('3', '1')] = {'capacity': link_a, 'usage': 0}
links_map_c[('2', '3')] = links_map_c[('11', '1')] = {'capacity': link_c, 'usage': 0}
links_map_c[('3', '2')] = links_map_c[('11', '2')] = {'capacity': link_c, 'usage': 0}
links_map_c[('4', '1')] = links_map_c[('5', '1')] = {'capacity': link_b, 'usage': 0}
links_map_c[('4', '2')] = links_map_c[('11', '3')] = {'capacity': link_a, 'usage': 0}
links_map_c[('5', '2')] = links_map_c[('8', '1')] = {'capacity': link_b, 'usage': 0}
links_map_c[('6', '1')] = links_map_c[('8', '2')] = {'capacity': link_a, 'usage': 0}
links_map_c[('6', '2')] = links_map_c[('12', '1')] = {'capacity': link_a, 'usage': 0}
links_map_c[('7', '1')] = links_map_c[('10', '2')] = {'capacity': link_a, 'usage': 0}
links_map_c[('7', '2')] = links_map_c[('12', '2')] = {'capacity': link_a, 'usage': 0}
links_map_c[('8', '3')] = links_map_c[('9', '1')] = {'capacity': link_d, 'usage': 0}
links_map_c[('9', '2')] = links_map_c[('10', '3')] = {'capacity': link_d, 'usage': 0}
links_map_c[('9', '3')] = links_map_c[('11', '4')] = {'capacity': link_b, 'usage': 0}
links_map_c[('10', '4')] = links_map_c[('11', '5')] = {'capacity': link_c, 'usage': 0}
links_map_c[('10', '5')] = links_map_c[('12', '3')] = {'capacity': link_c, 'usage': 0}

links_map_c[('1', '3')] = {'capacity': link_z}
links_map_c[('2', '4')] = {'capacity': link_z}
links_map_c[('3', '3')] = {'capacity': link_z}
links_map_c[('4', '3')] = {'capacity': link_z}
links_map_c[('5', '3')] = {'capacity': link_z}
links_map_c[('6', '3')] = {'capacity': link_z}
links_map_c[('7', '3')] = {'capacity': link_z}
