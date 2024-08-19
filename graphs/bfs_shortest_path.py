from collections import deque

def bfs_shortest_path(adjacency_list, start):
    """
       Breadth first search on a graph

       :param adjacency_list: adjacency list describing the graph
       :param start: starting node
       :return: length of shortest path from starting node, -1 if unreachable
    """
    n = len(adjacency_list)
    distance = [float("inf")] * n
    distance[start] = 0
    Q = deque()
    Q.append(start)
    vis = set()

    while len(Q):
        u = Q.popleft()
        if u not in vis:
            vis.add(u)
            for v in adjacency_list[u]:
                if  distance[u] + 1 < distance[v]:
                    distance[v] = distance[u] + 1
                    if v not in vis: 
                        Q.append(v)
    return distance
