import heapq
def prim(G):
    n = len(G)
    vis = [False] * n
    vis[0] = True
    Q = []
    for v, cost in G[0]:
        Q.append((cost, v))
    heapq.heapify(Q)
    res = 0

    while len(Q):
        cost, u = heapq.heappop(Q)
        if not vis[u]:
            vis[u] = True
            res += cost
            for v, cost in G[u]:
                heapq.heappush(Q, (cost, v))
    return res