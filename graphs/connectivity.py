def articulation(G):
    # assumes G is connected
    MAX_NODE = 1000000
    n = len(G)
    dfs = [MAX_NODE] * n
    low = [0] * n 
    T = [0] * n
    cnt = 1

    def visit(u, cnt):
        dfs[u] = cnt 
        low[u] = dfs[u]
        cnt += 1
        for v in G[u]:
            if dfs[v] == MAX_NODE:
                T[u] += 1
                res, cnt = visit(v, cnt)
                low[u] = min(low[u], res)
            else:
                low[u] = min(low[u], dfs[v])
        return low[u], cnt


    visit(0, cnt)
    res = [False] * n
    for i in range(1, n):
        if low[i] >= dfs[i]:
            res[i] = True 
    if T[0] > 1:
        res[0] = True
    bridges = []
    for u in range(n):
        for v in G[u]:
            if low[v] > dfs[u]:
                bridges.append([u, v])
    return res, low, bridges