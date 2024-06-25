def bellman_ford(G, u):
    n = len(G)
    dist = [100000] * n 
    dist[u] = 0

    for _ in range(n):
        for u in range(n):
            for (v, cost) in G[u]:
                dist[v] = min(dist[v], dist[u] + cost)
    
    for u in range(n):
        for (v, cost) in G[u]:
            if dist[v] > dist[u] + cost:
                raise ValueError("Negative cycle!")
    return dist