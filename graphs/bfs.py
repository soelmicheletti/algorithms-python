def bfs(adjacency_list, start):
    """
       Breadth first search on a graph

       :param adjacency_list: adjacency list describing the graph
       :param start: starting node
       :return: list of boolean indicating whether the corresponding node has been visited in the bfs
    """
    n = len(adjacency_list)
    visited = [False] * n
    Q = [start]

    while len(Q) > 0:
        u = Q.pop(0)
        if not visited[u]:
            visited[u] = True
            for v in adjacency_list[u]:
                if v not in Q and not visited[v]:
                    Q.append(v)
    return visited
