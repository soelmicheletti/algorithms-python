class Node:
    def __init__(
            self,
            val: int,
            left=None,
            right=None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

def insert(root: Node, val: int) -> Node:
    if not root:
        return Node(val=val)
    if val <= root.val:
        root.left = insert(root.left, val)
        return root
    root.right = insert(root.right, val)
    return root

def search(root: Node, val: int) -> bool:
    if not root:
        return False
    if root.val == val:
        return True
    if root.val > val:
        return search(root.left, val)
    return search(root.right, val)

def _get_symm_succ(root: Node) -> Node:
    curr = root.right 
    while curr.left:
        curr = curr.left
    return curr

def delete(root: Node, val: int):
    "It assumes val is in the BST"
    if root.val == val:
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        symm_succ = _get_symm_succ(root)
        root.val = symm_succ.val
        root.right = delete(root.right, symm_succ.val)
        return root
    if val < root.val:
        root.left = delete(root.left, val)
        return root
    root.right = delete(root.right, val)
    return root

def pre_order(root: Node):
    if not root:
        return "None"
    return f"{root.val} ({pre_order(root.left)}) ({pre_order(root.right)})"