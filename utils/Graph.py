link_a = 10
link_b = 14
link_c = 20
link_d = 40
link_z = 424242  # Arbitrary high value

cap_a = link_a / 2
cap_b = link_b / 2
cap_c = link_c / 2
cap_d = link_d / 2
cap_z = link_z / 2

# Bidirectional dictionary of the hosts in the topology
host_mac_map = {
    'h1': '00:00:00:00:00:01', '00:00:00:00:00:01': 'h1',
    'h2': '00:00:00:00:00:02', '00:00:00:00:00:02': 'h2',
    'h3': '00:00:00:00:00:03', '00:00:00:00:00:03': 'h3',
    'h4': '00:00:00:00:00:04', '00:00:00:00:00:04': 'h4',
    'h5': '00:00:00:00:00:05', '00:00:00:00:00:05': 'h5',
    'h6': '00:00:00:00:00:06', '00:00:00:00:00:06': 'h6',
    'h7': '00:00:00:00:00:07', '00:00:00:00:00:07': 'h7'
}

# Bidirectional dictionary of the switches in the topology
switch_dpid_map = {
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

# ==========
# Topology A
# ==========
graph_a = {
    'h1': ['s1'],
    'h2': ['s2'],
    'h3': ['s3'],
    'h4': ['s4'],

    's1': ['h1', 's2', 's3', 's4'],
    's2': ['h2', 's1', 's3', 's4'],
    's3': ['h3', 's1', 's2', 's4'],
    's4': ['h4', 's1', 's2', 's3']
}

link_map_a = {
    'h1': {'s1': [4, {'capacity': cap_z, 'usage': 0}]},
    'h2': {'s2': [4, {'capacity': cap_z, 'usage': 0}]},
    'h3': {'s3': [4, {'capacity': cap_z, 'usage': 0}]},
    'h4': {'s4': [4, {'capacity': cap_z, 'usage': 0}]},
    's1': {
        'h1': [4, {'capacity': cap_z, 'usage': 0}],
        's2': [1, {'capacity': cap_a, 'usage': 0}],
        's3': [2, {'capacity': cap_d, 'usage': 0}],
        's4': [3, {'capacity': cap_b, 'usage': 0}]
    },
    's2': {
        'h2': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_a, 'usage': 0}],
        's3': [2, {'capacity': cap_c, 'usage': 0}],
        's4': [3, {'capacity': cap_c, 'usage': 0}]
    },
    's3': {
        'h3': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_d, 'usage': 0}],
        's2': [2, {'capacity': cap_c, 'usage': 0}],
        's4': [3, {'capacity': cap_a, 'usage': 0}]
    },
    's4': {
        'h4': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_b, 'usage': 0}],
        's2': [2, {'capacity': cap_c, 'usage': 0}],
        's3': [3, {'capacity': cap_a, 'usage': 0}]
    }
}

# ==========
# Topology B
# ==========
graph_b = {
    'h1': ['s1'],
    'h2': ['s5'],
    'h3': ['s2'],
    'h4': ['s6'],
    'h5': ['s9'],

    's1': ['h1', 's2', 's6', 's9'],
    's2': ['h3', 's1', 's3', 's4'],
    's3': ['s2', 's5'],
    's4': ['s2', 's5'],
    's5': ['h2', 's3', 's4'],
    's6': ['h4', 's1', 's7', 's8'],
    's7': ['s6', 's9'],
    's8': ['s6', 's9'],
    's9': ['h5', 's1', 's7', 's8']
}

link_map_b = {
    'h1': {'s1': [4, {'capacity': cap_z, 'usage': 0}]},
    'h2': {'s5': [4, {'capacity': cap_z, 'usage': 0}]},
    'h3': {'s2': [4, {'capacity': cap_z, 'usage': 0}]},
    'h4': {'s6': [4, {'capacity': cap_z, 'usage': 0}]},
    'h5': {'s9': [4, {'capacity': cap_z, 'usage': 0}]},
    's1': {
        'h1': [4, {'capacity': cap_z, 'usage': 0}],
        's2': [1, {'capacity': cap_d, 'usage': 0}],
        's6': [2, {'capacity': cap_b, 'usage': 0}],
        's9': [3, {'capacity': cap_a, 'usage': 0}]
    },
    's2': {
        'h3': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_d, 'usage': 0}],
        's3': [2, {'capacity': cap_a, 'usage': 0}],
        's4': [3, {'capacity': cap_d, 'usage': 0}]
    },
    's3': {
        's2': [1, {'capacity': cap_a, 'usage': 0}],
        's5': [2, {'capacity': cap_a, 'usage': 0}]
    },
    's4': {
        's2': [1, {'capacity': cap_d, 'usage': 0}],
        's5': [2, {'capacity': cap_d, 'usage': 0}]
    },
    's5': {
        'h2': [3, {'capacity': cap_z, 'usage': 0}],
        's3': [1, {'capacity': cap_a, 'usage': 0}],
        's4': [2, {'capacity': cap_d, 'usage': 0}]
    },
    's6': {
        'h4': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_b, 'usage': 0}],
        's7': [2, {'capacity': cap_a, 'usage': 0}],
        's8': [3, {'capacity': cap_c, 'usage': 0}]
    },
    's7': {
        's6': [1, {'capacity': cap_a, 'usage': 0}],
        's9': [2, {'capacity': cap_a, 'usage': 0}]
    },
    's8': {
        's6': [1, {'capacity': cap_c, 'usage': 0}],
        's9': [2, {'capacity': cap_c, 'usage': 0}]
    },
    's9': {
        'h5': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_a, 'usage': 0}],
        's7': [2, {'capacity': cap_a, 'usage': 0}],
        's8': [3, {'capacity': cap_c, 'usage': 0}]
    }
}

# ==========
# Topology C
# ==========
graph_c = {
    'h1': ['s1'],
    'h2': ['s2'],
    'h3': ['s3'],
    'h4': ['s4'],
    'h5': ['s5'],
    'h6': ['s6'],
    'h7': ['s7'],

    's1': ['h1', 's2', 's10'],
    's2': ['h2', 's1', 's3', 's11'],
    's3': ['h3', 's2', 's11'],
    's4': ['h4', 's5', 's11'],
    's5': ['h5', 's4', 's8'],
    's6': ['h6', 's8', 's12'],
    's7': ['h7', 's10', 's12'],
    's8': ['s5', 's6', 's9'],
    's9': ['s8', 's10', 's11'],
    's10': ['s1', 's7', 's9', 's11', 's12'],
    's11': ['s2', 's3', 's4', 's9', 's10'],
    's12': ['s6', 's7', 's10']
}

link_map_c = {
    'h1': {'s1': [3, {'capacity': cap_z, 'usage': 0}]},
    'h2': {'s2': [4, {'capacity': cap_z, 'usage': 0}]},
    'h3': {'s3': [3, {'capacity': cap_z, 'usage': 0}]},
    'h4': {'s4': [3, {'capacity': cap_z, 'usage': 0}]},
    'h5': {'s5': [3, {'capacity': cap_z, 'usage': 0}]},
    'h6': {'s6': [3, {'capacity': cap_z, 'usage': 0}]},
    'h7': {'s7': [3, {'capacity': cap_z, 'usage': 0}]},
    's1': {
        'h1': [3, {'capacity': cap_z, 'usage': 0}],
        's2': [1, {'capacity': cap_b, 'usage': 0}],
        's10': [2, {'capacity': cap_b, 'usage': 0}]
    },
    's2': {
        'h2': [4, {'capacity': cap_z, 'usage': 0}],
        's1': [1, {'capacity': cap_b, 'usage': 0}],
        's3': [2, {'capacity': cap_a, 'usage': 0}],
        's11': [3, {'capacity': cap_c, 'usage': 0}]
    },
    's3': {
        'h3': [3, {'capacity': cap_z, 'usage': 0}],
        's2': [1, {'capacity': cap_a, 'usage': 0}],
        's11': [2, {'capacity': cap_c, 'usage': 0}]
    },
    's4': {
        'h4': [3, {'capacity': cap_z, 'usage': 0}],
        's5': [1, {'capacity': cap_b, 'usage': 0}],
        's11': [2, {'capacity': cap_a, 'usage': 0}]
    },
    's5': {
        'h5': [3, {'capacity': cap_z, 'usage': 0}],
        's4': [1, {'capacity': cap_b, 'usage': 0}],
        's8': [2, {'capacity': cap_b, 'usage': 0}]
    },
    's6': {
        'h6': [3, {'capacity': cap_z, 'usage': 0}],
        's8': [1, {'capacity': cap_a, 'usage': 0}],
        's12': [2, {'capacity': cap_a, 'usage': 0}]
    },
    's7': {
        'h7': [3, {'capacity': cap_z, 'usage': 0}],
        's10': [1, {'capacity': cap_a, 'usage': 0}],
        's12': [2, {'capacity': cap_a, 'usage': 0}]
    },
    's8': {
        's5': [1, {'capacity': cap_b, 'usage': 0}],
        's6': [2, {'capacity': cap_c, 'usage': 0}],
        's9': [3, {'capacity': cap_d, 'usage': 0}]
    },
    's9': {
        's8': [1, {'capacity': cap_d, 'usage': 0}],
        's10': [2, {'capacity': cap_d, 'usage': 0}],
        's11': [3, {'capacity': cap_b, 'usage': 0}]
    },
    's10': {
        's1': [1, {'capacity': cap_b, 'usage': 0}],
        's7': [2, {'capacity': cap_a, 'usage': 0}],
        's9': [3, {'capacity': cap_d, 'usage': 0}],
        's11': [4, {'capacity': cap_a, 'usage': 0}],
        's12': [5, {'capacity': cap_c, 'usage': 0}]
    },
    's11': {
        's2': [1, {'capacity': cap_c, 'usage': 0}],
        's3': [2, {'capacity': cap_c, 'usage': 0}],
        's4': [3, {'capacity': cap_a, 'usage': 0}],
        's9': [4, {'capacity': cap_b, 'usage': 0}],
        's10': [5, {'capacity': cap_a, 'usage': 0}]
    },
    's12': {
        's6': [1, {'capacity': cap_a, 'usage': 0}],
        's7': [2, {'capacity': cap_a, 'usage': 0}],
        's10': [3, {'capacity': cap_c, 'usage': 0}]
    }
}
