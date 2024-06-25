import heapq
def bfs_shortest_path(adjacency_list, start):
    """
       Breadth first search on a graph

       :param adjacency_list: adjacency list describing the graph
       :param start: starting node
       :return: length of shortest path from starting node, -1 if unreachable
    """
    n = len(adjacency_list)
    distance = [-1] * n
    distance[start] = 0
    Q = [start]
    heapq.heapify(Q)

    while len(Q) > 0:
        u = heapq.heappop(Q)

        for v in adjacency_list[u]:
            if distance[v] == -1 or distance[u] + 1 < distance[v]:
                distance[v] = distance[u] + 1
                heapq.heappush(Q, v)
    return distance
