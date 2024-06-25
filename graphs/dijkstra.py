import heapq
def dijkstra(G, start):
    n = len(G)
    d = [100000] * n
    d[start] = 0
    Q = [(0, start)]
    heapq.heapify(Q)

    while len(Q):
        _, u = heapq.heappop(Q)
        for v, cost in G[u]:
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heapq.heappush(Q, (d[v], v))
    return d