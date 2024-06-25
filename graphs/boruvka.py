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

def boruvka(G):
    n = len(G)
    nodes = []
    res = 0
    
    for i in range(n): nodes.append(make_set(i))

    for _ in range(n):
        cheapest = [-1] * n
        for u in range(n):
            for v, w in G[u]:
                if find(nodes[u]).val != find(nodes[v]).val:
                    if cheapest[find(nodes[u]).val] == -1 or w < cheapest[find(nodes[u]).val][1]:
                        cheapest[find(nodes[u]).val] = (v, w)
                    if cheapest[find(nodes[v]).val] == -1 or w < cheapest[find(nodes[v]).val][1]:
                        cheapest[find(nodes[v]).val] = (u, w)
        for u in range(n):
            if cheapest[u] != -1:
                v, w = cheapest[u] 
                if find(nodes[u]).val != find(nodes[v]).val:
                    union(nodes[u], nodes[v])
                    res += w 
    return res

                
