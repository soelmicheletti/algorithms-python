def topo_sort(G):
    n = len(G)
    deg = [0] * n

    for u in range(n):
        for v in G[u]:
            deg[v] += 1
    
    S = []
    res = [-1] * n
    for u in range(n):
        if deg[u] == 0:
            S.append(u)
    
    cnt = 0
    while len(S):
        u = S.pop()
        res[u] = cnt
        cnt += 1
        for v in G[u]:
            deg[v] -= 1
            if deg[v] == 0:
                S.append(v)
    
    if cnt < n:
        raise ValueError("No topological sorting!")
    return res