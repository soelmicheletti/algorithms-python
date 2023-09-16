def dfs(adjacency_list, start):
    """
       Depth first search on a graph

       :param adjacency_list: adjacency list describing the graph
       :param start: starting node
       :return: list of boolean indicating whether the corresponding node has been visited in the dfs
    """
    n = len(adjacency_list)
    visited = [False] * n
    S = [start]

    while len(S) > 0:
        u = S.pop(0)
        if not visited[u]:
            visited[u] = True
            for v in adjacency_list[u]:
                if not visited[v]:
                    S = [v] + S
    return visited
