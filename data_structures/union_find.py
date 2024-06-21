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
