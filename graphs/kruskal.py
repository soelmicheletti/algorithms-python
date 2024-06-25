class Node:
    def __init__(self, val: int) -> None:
        self.val=val
        self.parent = self 
    
def make_set(val: int) -> Node:
    return Node(val)

def find(start: Node) -> Node:
    while start.parent != start:
        start = start.parent
    return start

def union(a: Node, b: Node):
    a_length = 0
    while a.parent != a:
        a = a.parent
        a_length += 1
    
    b_length = 0
    while b.parent != b:
        b = b.parent
        b_length += 1
    
    if a_length <= b_length:
        b.parent = a
    else:
        a.parent = b


def kruskal(G):
    n = len(G)
    nodes = []
    L = []
    for u in range(n):
        nodes.append(make_set(u))
        for e in G[u]:
            L.append((e[1], u, e[0]))
    L = sorted(L)
    res = 0
    for cost, u, v in L:
        if find(nodes[u]) != find(nodes[v]):
            res += cost
            union(nodes[u], nodes[v])
    return res