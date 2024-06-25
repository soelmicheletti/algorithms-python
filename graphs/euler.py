def eulerian_circuit(G):
    # assumes G has an Eulerian circuit
    n = len(G)
    vis = set()

    def random_tour(u):
        tour = [u]
        curr = None 
        for v in G[u]:
            if (u, v) not in vis and (v, u) not in vis:
                vis.add((u, v))
                curr = v
                tour.append(v)
                break
 
        if not curr:
            return []
        
        while curr != u:
            for v in G[curr]:
                if (curr, v) not in vis and (v, curr) not in vis:
                    vis.add((curr, v))
                    tour.append(v)
                    curr = v
        return tour


    res = random_tour(0)
    slow = 0
    while slow != n:
        app = []
        for v in G[res[slow]]:
            if (res[slow], v) not in vis and (v, res[slow]) not in vis:
                app = random_tour(slow)
                res = res[0:slow] + app + res[slow+1:]
        slow += 1
    return res
