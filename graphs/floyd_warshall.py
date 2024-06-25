def floy_warshall(G):
    # G is given ad adjacency matrix
    n = len(G)
    max_val = 100000
    d = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(max_val)
        d.append(tmp)
    
    for i in range(n): d[i][i] = 0
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                d[u][v] = G[u][v]

    for k in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
    return d

