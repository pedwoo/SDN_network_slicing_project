def pathfinding(graph, src, dst, path=None):
    if path is None:
        path = []
    path = path + [src]  # Append the current node to the path

    if src == dst:  # Base case: If we reached the destination
        return path

    if src not in graph:  # If the node has no neighbors, return None
        return None

    shortest = None  # To store the shortest path found
    for neighbor in graph[src]:  # Iterate over neighbors
        if neighbor not in path:  # Avoid cycles
            new_path = pathfinding(graph, neighbor, dst, path)  # Recursive call
            if new_path:
                if shortest is None or len(new_path) < len(shortest):  # Keep the shortest path
                    shortest = new_path

    return shortest  # Return the shortest path found, or None if no path exists


def filter_graph(graph, usage_map, required):
    filtered_graph = dict()

    for node in graph:
        for neighbor in graph[node]:
            if usage_map[node][neighbor][1]['capacity'] - usage_map[node][neighbor][1]['usage'] >= required:
                if node not in filtered_graph:
                    filtered_graph[node] = list()
                filtered_graph[node].append(neighbor)

    return filtered_graph


def find_shortest_path(graph, usage_map, src, dst, required):
    filtered_graph = filter_graph(graph, usage_map, required)
    return pathfinding(filtered_graph, src, dst)


# if __name__ == '__main__':
#     # ===========
#     # Test
#     # ===========
#     Graph = graph_c
#     PortMap = port_map_c
#     UsageMap = usage_map_c
#
#     src_host = 'h1'
#     dst_host = 'h5'
#     capacity = 5
#     p = find_shortest_path(Graph, UsageMap, src_host, dst_host, capacity)
#
#     flows = list()
#
#     if p:
#         print(f"Path from {src_host} to {dst_host}, capacity: {capacity}: {p}")
#         in_port = None
#         out_port = None
#
#         for i in range(1, (len(p) - 1)):
#             in_port = PortMap[p[i]][p[i - 1]]
#             out_port = PortMap[p[i]][p[i + 1]]
#             flows.append((p[i], src_host, dst_host, in_port, out_port, capacity))
#
#     print('===')
#     print('Flows to install')
#     for f in flows:
#         print(f)
