configurations = {
    'a': {  # Default configurations for topology A
        0: [
            # All -> All on 4Mbps (2Mbps bidirectional) links

            # s1 links
            (1, 'h1', 'h2', 4, 1, 1, 2, False), (1, 'h2', 'h1', 1, 4, 1, 2, False),
            (1, 'h1', 'h3', 4, 2, 1, 2, False), (1, 'h3', 'h1', 2, 4, 1, 2, False),
            (1, 'h1', 'h4', 4, 3, 1, 2, False), (1, 'h4', 'h1', 3, 4, 1, 2, False),

            # s2 links
            (2, 'h2', 'h1', 4, 1, 1, 2, False), (2, 'h1', 'h2', 1, 4, 1, 2, False),
            (2, 'h2', 'h3', 4, 2, 1, 2, False), (2, 'h3', 'h2', 2, 4, 1, 2, False),
            (2, 'h2', 'h4', 4, 3, 1, 2, False), (2, 'h4', 'h2', 3, 4, 1, 2, False),

            # s3 links
            (3, 'h3', 'h1', 4, 1, 1, 2, False), (3, 'h1', 'h3', 1, 4, 1, 2, False),
            (3, 'h3', 'h2', 4, 2, 1, 2, False), (3, 'h2', 'h3', 2, 4, 1, 2, False),
            (3, 'h3', 'h4', 4, 3, 1, 2, False), (3, 'h4', 'h3', 3, 4, 1, 2, False),

            # s4 links
            (4, 'h4', 'h1', 4, 1, 1, 2, False), (4, 'h1', 'h4', 1, 4, 1, 2, False),
            (4, 'h4', 'h2', 4, 2, 1, 2, False), (4, 'h2', 'h4', 2, 4, 1, 2, False),
            (4, 'h4', 'h3', 4, 3, 1, 2, False), (4, 'h3', 'h4', 3, 4, 1, 2, False)
        ],
        1: [
            # All -> All on maximum capacity links

            # s1 links
            (1, 'h1', 'h2', 4, 1, 1, 2, False), (1, 'h2', 'h1', 1, 4, 1, 42, False),
            (1, 'h1', 'h3', 4, 2, 1, 10, False), (1, 'h3', 'h1', 2, 4, 1, 42, False),
            (1, 'h1', 'h4', 4, 3, 1, 3, False), (1, 'h4', 'h1', 3, 4, 1, 42, False),

            # s2 links
            (2, 'h2', 'h1', 4, 1, 1, 2, False), (2, 'h1', 'h2', 1, 4, 1, 42, False),
            (2, 'h2', 'h3', 4, 2, 1, 5, False), (2, 'h3', 'h2', 2, 4, 1, 42, False),
            (2, 'h2', 'h4', 4, 3, 1, 5, False), (2, 'h4', 'h2', 3, 4, 1, 42, False),

            # s3 links
            (3, 'h3', 'h1', 4, 1, 1, 10, False), (3, 'h1', 'h3', 1, 4, 1, 42, False),
            (3, 'h3', 'h2', 4, 2, 1, 5, False), (3, 'h2', 'h3', 2, 4, 1, 42, False),
            (3, 'h3', 'h4', 4, 3, 1, 2, False), (3, 'h4', 'h3', 3, 4, 1, 42, False),

            # s4 links
            (4, 'h4', 'h1', 4, 1, 1, 3, False), (4, 'h1', 'h4', 1, 4, 1, 42, False),
            (4, 'h4', 'h2', 4, 2, 1, 5, False), (4, 'h2', 'h4', 2, 4, 1, 42, False),
            (4, 'h4', 'h3', 4, 3, 1, 2, False), (4, 'h3', 'h4', 3, 4, 1, 42, False)
        ],
        2: [
            # h3 -> h4 on 8Mbps (4Mbps bidirectional) link through s2
            # h3 -> h2 on 2Mbps (1Mbps bidirectional) link

            # h3 -> h4 on 8Mbps (4Mbps bidirectional) link through s2
            (3, 'h3', 'h4', 4, 2, 1, 4, False), (3, 'h4', 'h3', 2, 4, 1, 4, False),
            (4, 'h4', 'h3', 4, 2, 1, 4, False), (4, 'h3', 'h4', 2, 4, 1, 4, False),
            (2, 'h3', 'h4', 2, 3, 1, 4, False), (2, 'h4', 'h3', 3, 2, 1, 4, False),

            # h3 -> h2 on 2Mbps (1Mbps bidirectional) link
            (3, 'h3', 'h2', 4, 2, 1, 1, False), (3, 'h2', 'h3', 2, 4, 1, 1, False),
            (2, 'h2', 'h3', 4, 2, 1, 1, False), (2, 'h3', 'h2', 2, 4, 1, 1, False)
        ],
        3: [
            # h3 -> h1 on 10Mbps (5Mbps bidirectional) link
            # h2 -> h1 on 10Mbps (5Mbps bidirectional) link through s3

            # h3 -> h1 on 10Mbps (5Mbps bidirectional) link
            (3, 'h3', 'h1', 4, 1, 1, 5, False), (3, 'h1', 'h3', 1, 4, 1, 5, False),
            (1, 'h1', 'h3', 4, 2, 1, 5, False), (1, 'h3', 'h1', 2, 4, 1, 5, False),

            # h2 -> h1 on 10Mbps (5Mbps bidirectional) link through s3
            (2, 'h2', 'h1', 4, 2, 1, 5, False), (2, 'h1', 'h2', 2, 4, 1, 5, False),
            (3, 'h2', 'h1', 2, 1, 1, 5, False), (3, 'h1', 'h2', 1, 2, 1, 5, False),
            (1, 'h1', 'h2', 4, 2, 1, 5, False), (1, 'h2', 'h1', 2, 4, 1, 5, False)
        ]
    },
    'b': {  # Default configurations for topology B
        0: [
            # Only configured flows on switches that have a host connected to them, based on the shortest path between the hosts
            # All links are 1Mbps bidirectional (2Mbps total) links

            # s1 links
            (1, 'h1', 'h2', 4, 1, 1, 1, False), (1, 'h2', 'h1', 1, 4, 1, 1, False),
            (1, 'h1', 'h3', 4, 1, 1, 1, False), (1, 'h3', 'h1', 1, 4, 1, 1, False),
            (1, 'h1', 'h4', 4, 2, 1, 1, False), (1, 'h4', 'h1', 2, 4, 1, 1, False),
            (1, 'h1', 'h5', 4, 3, 1, 1, False), (1, 'h5', 'h1', 3, 4, 1, 1, False),

            # s2 links
            (2, 'h3', 'h1', 4, 1, 1, 1, False), (2, 'h1', 'h3', 1, 4, 1, 1, False),
            (2, 'h3', 'h2', 4, 3, 1, 1, False), (2, 'h2', 'h3', 3, 4, 1, 1, False),
            (2, 'h3', 'h4', 4, 1, 1, 1, False), (2, 'h4', 'h3', 1, 4, 1, 1, False),
            (2, 'h3', 'h5', 4, 1, 1, 1, False), (2, 'h5', 'h3', 1, 4, 1, 1, False),

            # s5 links
            (5, 'h2', 'h1', 3, 2, 1, 1, False), (5, 'h1', 'h2', 2, 3, 1, 1, False),
            (5, 'h2', 'h3', 3, 2, 1, 1, False), (5, 'h3', 'h2', 2, 3, 1, 1, False),
            (5, 'h2', 'h4', 3, 2, 1, 1, False), (5, 'h4', 'h2', 2, 3, 1, 1, False),
            (5, 'h2', 'h5', 3, 2, 1, 1, False), (5, 'h5', 'h2', 2, 3, 1, 1, False),

            # s6 links
            (6, 'h4', 'h1', 4, 3, 1, 1, False), (6, 'h1', 'h4', 3, 4, 1, 1, False),
            (6, 'h4', 'h2', 4, 3, 1, 1, False), (6, 'h2', 'h4', 3, 4, 1, 1, False),
            (6, 'h4', 'h3', 4, 3, 1, 1, False), (6, 'h3', 'h4', 3, 4, 1, 1, False),
            (6, 'h4', 'h5', 4, 2, 1, 1, False), (6, 'h5', 'h4', 2, 4, 1, 1, False),

            # s9 links
            (9, 'h5', 'h1', 4, 3, 1, 1, False), (9, 'h1', 'h5', 3, 4, 1, 1, False),
            (9, 'h5', 'h2', 4, 3, 1, 1, False), (9, 'h2', 'h5', 3, 4, 1, 1, False),
            (9, 'h5', 'h3', 4, 3, 1, 1, False), (9, 'h3', 'h5', 3, 4, 1, 1, False),
            (9, 'h5', 'h4', 4, 2, 1, 1, False), (9, 'h4', 'h5', 2, 4, 1, 1, False)
        ],
        1: [
            # h1 -> h2 on 4Mbps (2Mbps bidirectional) link through s2, s4
            # h1 -> h4 on 2Mbps (1Mbps bidirectional) link through s9, s8
            # h2 -> h3 on 16Mbps (8Mbps bidirectional) link through s4
            # h3 -> h4 on 4Mbps (2Mbps bidirectional) link through s1
            # h4 -> h5 on 6Mbps (3Mbps bidirectional) link through s8

            # h1 -> h2 on 4Mbps (2Mbps bidirectional) link through s2, s4
            (1, 'h1', 'h2', 4, 1, 1, 2, False), (1, 'h2', 'h1', 1, 4, 1, 2, False),
            (2, 'h1', 'h2', 1, 3, 1, 2, False), (2, 'h2', 'h1', 3, 1, 1, 2, False),
            (4, 'h1', 'h2', 1, 2, 1, 2, False), (4, 'h2', 'h1', 2, 1, 1, 2, False),
            (5, 'h1', 'h2', 2, 3, 1, 2, False), (5, 'h2', 'h1', 3, 2, 1, 2, False),

            # h1 -> h4 on 2Mbps (1Mbps bidirectional) link through s9, s8
            (1, 'h1', 'h4', 4, 3, 1, 1, False), (1, 'h4', 'h1', 3, 4, 1, 1, False),
            (9, 'h1', 'h4', 1, 3, 1, 1, False), (9, 'h4', 'h1', 3, 1, 1, 1, False),
            (8, 'h1', 'h4', 2, 1, 1, 1, False), (8, 'h4', 'h1', 1, 2, 1, 1, False),
            (6, 'h1', 'h4', 3, 4, 1, 1, False), (6, 'h4', 'h1', 4, 3, 1, 1, False),

            # h2 -> h3 on 16Mbps (6Mbps bidirectional) link through s4
            (5, 'h2', 'h3', 3, 2, 1, 8, False), (5, 'h3', 'h2', 2, 3, 1, 8, False),
            (4, 'h2', 'h3', 2, 1, 1, 8, False), (4, 'h3', 'h2', 1, 2, 1, 8, False),
            (2, 'h2', 'h3', 3, 4, 1, 8, False), (2, 'h3', 'h2', 4, 3, 1, 8, False),

            # h3 -> h4 on 4Mbps (2Mbps bidirectional) link through s1
            (2, 'h3', 'h4', 4, 1, 1, 2, False), (2, 'h4', 'h3', 1, 4, 1, 2, False),
            (1, 'h3', 'h4', 1, 2, 1, 2, False), (1, 'h4', 'h3', 2, 1, 1, 2, False),
            (6, 'h3', 'h4', 1, 4, 1, 2, False), (6, 'h4', 'h3', 4, 1, 1, 2, False),

            # h4 -> h5 on 6Mbps (3Mbps bidirectional) link through s8
            (6, 'h4', 'h5', 4, 3, 1, 3, False), (6, 'h5', 'h4', 3, 4, 1, 3, False),
            (8, 'h4', 'h5', 1, 2, 1, 3, False), (8, 'h5', 'h4', 2, 1, 1, 3, False),
            (9, 'h4', 'h5', 3, 4, 1, 3, False), (9, 'h5', 'h4', 4, 3, 1, 3, False)
        ]
    },
    'c': {  # Default configurations for topology C
        0: [
            # Only configured flows on switches that have a host connected to them, based on the shortest path between the hosts
            # All links are 1Mbps bidirectional (2Mbps total) links

            # s1 links
            (1, 'h1', 'h2', 3, 1, 1, 1, False), (1, 'h2', 'h1', 1, 3, 1, 1, False),
            (1, 'h1', 'h3', 3, 1, 1, 1, False), (1, 'h3', 'h1', 1, 3, 1, 1, False),
            (1, 'h1', 'h4', 3, 1, 1, 1, False), (1, 'h4', 'h1', 1, 3, 1, 1, False),
            (1, 'h1', 'h5', 3, 2, 1, 1, False), (1, 'h5', 'h1', 2, 3, 1, 1, False),
            (1, 'h1', 'h6', 3, 2, 1, 1, False), (1, 'h6', 'h1', 2, 3, 1, 1, False),
            (1, 'h1', 'h7', 3, 2, 1, 1, False), (1, 'h7', 'h1', 2, 3, 1, 1, False),

            # s2 links
            (2, 'h2', 'h1', 4, 1, 1, 1, False), (2, 'h1', 'h2', 1, 4, 1, 1, False),
            (2, 'h2', 'h3', 4, 2, 1, 1, False), (2, 'h3', 'h2', 2, 4, 1, 1, False),
            (2, 'h2', 'h4', 4, 3, 1, 1, False), (2, 'h4', 'h2', 3, 4, 1, 1, False),
            (2, 'h2', 'h5', 4, 3, 1, 1, False), (2, 'h5', 'h2', 3, 4, 1, 1, False),
            (2, 'h2', 'h6', 4, 3, 1, 1, False), (2, 'h6', 'h2', 3, 4, 1, 1, False),
            (2, 'h2', 'h7', 4, 1, 1, 1, False), (2, 'h7', 'h2', 1, 4, 1, 1, False),

            # s3 links
            (3, 'h3', 'h1', 3, 1, 1, 1, False), (3, 'h1', 'h3', 1, 3, 1, 1, False),
            (3, 'h3', 'h2', 3, 1, 1, 1, False), (3, 'h2', 'h3', 1, 3, 1, 1, False),
            (3, 'h3', 'h4', 3, 2, 1, 1, False), (3, 'h4', 'h3', 2, 3, 1, 1, False),
            (3, 'h3', 'h5', 3, 2, 1, 1, False), (3, 'h5', 'h3', 2, 3, 1, 1, False),
            (3, 'h3', 'h6', 3, 2, 1, 1, False), (3, 'h6', 'h3', 2, 3, 1, 1, False),
            (3, 'h3', 'h7', 3, 2, 1, 1, False), (3, 'h7', 'h3', 2, 3, 1, 1, False),

            # s4 links
            (4, 'h4', 'h1', 3, 2, 1, 1, False), (4, 'h1', 'h4', 2, 3, 1, 1, False),
            (4, 'h4', 'h2', 3, 2, 1, 1, False), (4, 'h2', 'h4', 2, 3, 1, 1, False),
            (4, 'h4', 'h3', 3, 2, 1, 1, False), (4, 'h3', 'h4', 2, 3, 1, 1, False),
            (4, 'h4', 'h5', 3, 1, 1, 1, False), (4, 'h5', 'h4', 1, 3, 1, 1, False),
            (4, 'h4', 'h6', 3, 1, 1, 1, False), (4, 'h6', 'h4', 1, 3, 1, 1, False),
            (4, 'h4', 'h7', 3, 1, 1, 1, False), (4, 'h7', 'h4', 1, 3, 1, 1, False),

            # s5 links
            (5, 'h5', 'h1', 3, 2, 1, 1, False), (5, 'h1', 'h5', 2, 3, 1, 1, False),
            (5, 'h5', 'h2', 3, 1, 1, 1, False), (5, 'h2', 'h5', 1, 3, 1, 1, False),
            (5, 'h5', 'h3', 3, 1, 1, 1, False), (5, 'h3', 'h5', 1, 3, 1, 1, False),
            (5, 'h5', 'h4', 3, 1, 1, 1, False), (5, 'h4', 'h5', 1, 3, 1, 1, False),
            (5, 'h5', 'h6', 3, 2, 1, 1, False), (5, 'h6', 'h5', 2, 3, 1, 1, False),
            (5, 'h5', 'h7', 3, 2, 1, 1, False), (5, 'h7', 'h5', 2, 3, 1, 1, False),

            # s6 links
            (6, 'h6', 'h1', 3, 2, 1, 1, False), (6, 'h1', 'h6', 2, 3, 1, 1, False),
            (6, 'h6', 'h2', 3, 2, 1, 1, False), (6, 'h2', 'h6', 2, 3, 1, 1, False),
            (6, 'h6', 'h3', 3, 1, 1, 1, False), (6, 'h3', 'h6', 1, 3, 1, 1, False),
            (6, 'h6', 'h4', 3, 1, 1, 1, False), (6, 'h4', 'h6', 1, 3, 1, 1, False),
            (6, 'h6', 'h5', 3, 1, 1, 1, False), (6, 'h5', 'h6', 1, 3, 1, 1, False),
            (6, 'h6', 'h7', 3, 2, 1, 1, False), (6, 'h7', 'h6', 2, 3, 1, 1, False),

            # s7 links
            (7, 'h7', 'h1', 3, 1, 1, 1, False), (7, 'h1', 'h7', 1, 3, 1, 1, False),
            (7, 'h7', 'h2', 3, 1, 1, 1, False), (7, 'h2', 'h7', 1, 3, 1, 1, False),
            (7, 'h7', 'h3', 3, 1, 1, 1, False), (7, 'h3', 'h7', 1, 3, 1, 1, False),
            (7, 'h7', 'h4', 3, 2, 1, 1, False), (7, 'h4', 'h7', 2, 3, 1, 1, False),
            (7, 'h7', 'h5', 3, 2, 1, 1, False), (7, 'h5', 'h7', 2, 3, 1, 1, False),
            (7, 'h7', 'h6', 3, 2, 1, 1, False), (7, 'h6', 'h7', 2, 3, 1, 1, False),
        ],
        1: [
            # h1 -> h6 on 2Mbps (1Mbps bidirectional) link through s10, s12
            # h2 -> h5 on 2Mbps (1Mbps bidirectional) link through s1, s10, s9, s8
            # h2 -> h7 on 4Mbps (2Mbps bidirectional) link through s11, s10, s12
            # h3 -> h4 on 4Mbps (2Mbps bidirectional) link through s11
            # h3 -> h7 on 2Mbps (1Mbps bidirectional) link through s11, s10
            # h4 -> h5 on 2Mbps (1Mbps bidirectional) link
            # h4 -> h6 on 4Mbps (2Mbps bidirectional) link through s8, s5

            # h1 -> h6 on 2Mbps (1Mbps bidirectional) link through s10, s12
            (1, 'h1', 'h6', 3, 2, 1, 1, False), (1, 'h6', 'h1', 2, 3, 1, 1, False),
            (10, 'h1', 'h6', 1, 5, 1, 1, False), (10, 'h6', 'h1', 5, 1, 1, 1, False),
            (12, 'h1', 'h6', 3, 1, 1, 1, False), (12, 'h6', 'h1', 1, 3, 1, 1, False),
            (6, 'h1', 'h6', 2, 3, 1, 1, False), (6, 'h6', 'h1', 3, 2, 1, 1, False),

            # h2 -> h5 on 2Mbps (1Mbps bidirectional) link through s1, s10, s9, s8
            (2, 'h2', 'h5', 4, 1, 1, 1, False), (2, 'h5', 'h2', 1, 4, 1, 1, False),
            (1, 'h2', 'h5', 1, 2, 1, 1, False), (1, 'h5', 'h2', 2, 1, 1, 1, False),
            (10, 'h2', 'h5', 1, 3, 1, 1, False), (10, 'h5', 'h2', 3, 1, 1, 1, False),
            (9, 'h2', 'h5', 2, 1, 1, 1, False), (9, 'h5', 'h2', 1, 2, 1, 1, False),
            (8, 'h2', 'h5', 3, 1, 1, 1, False), (8, 'h5', 'h2', 1, 3, 1, 1, False),
            (5, 'h2', 'h5', 2, 3, 1, 1, False), (5, 'h5', 'h2', 3, 2, 1, 1, False),

            # h2 -> h7 on 4Mbps (2Mbps bidirectional) link through s11, s10, s12
            (2, 'h2', 'h7', 4, 3, 1, 2, False), (2, 'h7', 'h2', 3, 4, 1, 2, False),
            (11, 'h2', 'h7', 1, 5, 1, 2, False), (11, 'h7', 'h2', 5, 1, 1, 2, False),
            (10, 'h2', 'h7', 4, 5, 1, 2, False), (10, 'h7', 'h2', 5, 4, 1, 2, False),
            (12, 'h2', 'h7', 3, 2, 1, 2, False), (12, 'h7', 'h2', 2, 3, 1, 2, False),
            (7, 'h2', 'h7', 2, 3, 1, 2, False), (7, 'h7', 'h2', 3, 2, 1, 2, False),

            # h3 -> h4 on 4Mbps (2Mbps bidirectional) link through s11
            (3, 'h3', 'h4', 3, 2, 1, 2, False), (3, 'h4', 'h3', 2, 3, 1, 2, False),
            (11, 'h3', 'h4', 2, 3, 1, 2, False), (11, 'h4', 'h3', 3, 2, 1, 2, False),
            (4, 'h3', 'h4', 2, 3, 1, 2, False), (4, 'h4', 'h3', 3, 2, 1, 2, False),

            # h3 -> h7 on 2Mbps (1Mbps bidirectional) link through s11, s10
            (3, 'h3', 'h7', 3, 2, 1, 1, False), (3, 'h7', 'h3', 2, 3, 1, 1, False),
            (11, 'h3', 'h7', 2, 5, 1, 1, False), (11, 'h7', 'h3', 5, 2, 1, 1, False),
            (10, 'h3', 'h7', 4, 2, 1, 1, False), (10, 'h7', 'h3', 2, 4, 1, 1, False),
            (7, 'h3', 'h7', 1, 3, 1, 1, False), (7, 'h7', 'h3', 3, 1, 1, 1, False),

            # h4 -> h5 on 2Mbps (1Mbps bidirectional) link
            (4, 'h4', 'h5', 3, 1, 1, 1, False), (4, 'h5', 'h4', 1, 3, 1, 1, False),
            (5, 'h4', 'h5', 1, 3, 1, 1, False), (5, 'h5', 'h4', 3, 1, 1, 1, False),

            # h4 -> h6 on 4Mbps (2Mbps bidirectional) link through s8, s5
            (4, 'h4', 'h6', 3, 1, 1, 2, False), (4, 'h6', 'h4', 1, 3, 1, 2, False),
            (5, 'h4', 'h6', 1, 2, 1, 2, False), (5, 'h6', 'h4', 2, 1, 1, 2, False),
            (8, 'h4', 'h6', 1, 2, 1, 2, False), (8, 'h6', 'h4', 2, 1, 1, 2, False),
            (6, 'h4', 'h6', 1, 3, 1, 2, False), (6, 'h6', 'h4', 3, 1, 1, 2, False)
        ],
        2: [
            # h2 -> h5 on 6Mbps (3Mbps bidirectional) link through s1, s10, s9, s8, s5
            # h3 -> h6 on 2Mbps (1Mbps bidirectional) link through s11, s10, s12
            # h4 -> h7 on 4Mbps (2Mbps bidirectional) link through s11, s10
            # h4 -> h5 on 6Mbps (3Mbps bidirectional) link

            # h2 -> h5 on 6Mbps (3Mbps bidirectional) link through s1, s10, s9, s8, s5
            (2, 'h2', 'h5', 4, 1, 1, 3, False), (2, 'h5', 'h2', 1, 4, 1, 3, False),
            (1, 'h2', 'h5', 1, 2, 1, 3, False), (1, 'h5', 'h2', 2, 1, 1, 3, False),
            (10, 'h2', 'h5', 1, 3, 1, 3, False), (10, 'h5', 'h2', 3, 1, 1, 3, False),
            (9, 'h2', 'h5', 2, 1, 1, 3, False), (9, 'h5', 'h2', 1, 2, 1, 3, False),
            (8, 'h2', 'h5', 3, 1, 1, 3, False), (8, 'h5', 'h2', 1, 3, 1, 3, False),
            (5, 'h2', 'h5', 2, 3, 1, 3, False), (5, 'h5', 'h2', 3, 2, 1, 3, False),

            # h3 -> h6 on 2Mbps (1Mbps bidirectional) link through s11, s10, s12
            (3, 'h3', 'h6', 3, 2, 1, 1, False), (3, 'h6', 'h3', 2, 3, 1, 1, False),
            (11, 'h3', 'h6', 2, 5, 1, 1, False), (11, 'h6', 'h3', 5, 2, 1, 1, False),
            (10, 'h3', 'h6', 4, 5, 1, 1, False), (10, 'h6', 'h3', 5, 4, 1, 1, False),
            (12, 'h3', 'h6', 3, 1, 1, 1, False), (12, 'h6', 'h3', 1, 3, 1, 1, False),
            (6, 'h3', 'h6', 2, 3, 1, 1, False), (6, 'h6', 'h3', 3, 2, 1, 1, False),

            # h4 -> h7 on 4Mbps (2Mbps bidirectional) link through s11, s10
            (4, 'h4', 'h7', 3, 2, 1, 2, False), (4, 'h7', 'h4', 2, 3, 1, 2, False),
            (11, 'h4', 'h7', 3, 5, 1, 2, False), (11, 'h7', 'h4', 5, 3, 1, 2, False),
            (10, 'h4', 'h7', 4, 2, 1, 2, False), (10, 'h7', 'h4', 2, 4, 1, 2, False),
            (7, 'h4', 'h7', 1, 3, 1, 2, False), (7, 'h7', 'h4', 3, 1, 1, 2, False),

            # h4 -> h5 on 6Mbps (3Mbps bidirectional) link
            (4, 'h4', 'h5', 3, 1, 1, 3, False), (4, 'h5', 'h4', 1, 3, 1, 3, False),
            (5, 'h4', 'h5', 1, 3, 1, 3, False), (5, 'h5', 'h4', 3, 1, 1, 3, False),
        ]
    }
}
