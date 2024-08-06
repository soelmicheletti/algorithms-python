class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self) -> None:
        self.root = None

    def _h(self, root: Node):
        if not root:
            return 0
        return root.height

    def _bal(self, root: Node):
        if not root:
            return 0
        return self._h(root.left)-self._h(root.right)

    def _add(self, val: int, root: Node) -> Node:
        # assumes no duplicates
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self._add(val, root.left)
        if val > root.val:
            root.right = self._add(val, root.right)

        root.height = 1 + max(self._h(root.left), self._h(root.right))
        bal = self._bal(root)

        if bal > 1 and val < root.left.val:
            return self._right_rotation(root)
        elif bal > 1 and val > root.left.val:
            root.left = self._left_rotation(root.left)
            return self._right_rotation(root)
        elif bal < -1 and val > root.right.val:
            return self._left_rotation(root)
        elif bal < -1 and val < root.right.val:
            root.right = self._right_rotation(root.right)
            return self._left_rotation(root)
        return root

    def add(self, val: int) -> None:
        self.root = self._add(val, self.root)

    def _search(self, val: int, root: Node) -> bool:
        if not root:
            return False
        if val == root.val:
            return True
        elif val < root.val:
            return self._search(val, root.left)
        elif val > root.val:
            return self._search(val, root.right)

    def search(self, val) -> bool:
        return self._search(val, self.root)

    def _left_rotation(self, root: Node):
        right = root.right
        T = right.left
        right.left = root
        root.right = T

        root.height = 1+max(self._h(root.left), self._h(root.right))
        right.height = 1+max(self._h(right.left), self._h(right.right))

        return right

    def _right_rotation(self, root: Node):
        left = root.left
        T2 = left.right
        left.right = root
        root.left = T2

        root.height = 1+max(self._h(root.left), self._h(root.right))
        left.height = 1+max(self._h(left.left), self._h(left.right))

        return left

    def _pre_order(self, root: Node):
        if not root:
            return ""
        res = str(root.val)
        if root.left:
            res = res + "{" + self._pre_order(root.left) + "}"
        else:
            res = res + "{}"
        if root.right:
            res = res + "{" + self._pre_order(root.right) + "}"
        else:
            res = res + "{}"
        return res

    def pre_order(self):
        return self._pre_order(self.root)