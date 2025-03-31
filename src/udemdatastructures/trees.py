from typing import Any


class Node[T]:
    def __init__(self, data: T):
        self.data: T = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree[T]:

    def __init__(self, root=None, key=lambda x: x):
        self.root: Node[T] | None = root
        self.key = key
        self._size: int = 0

    def insert(self, data: T):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        self._size += 1

    def _insert(self, node: Node, data: T):
        # If the data is less than the node data, we go to the left
        if self.key(data) < self.key(node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def search(self, goal: Any) -> bool:
        return self._search(self.root, goal)

    def _search(self, node: Node, goal: Any) -> bool:
        if node is None:
            return False
        if self.key(node.data) == goal:
            return True
        if self.key(goal) < self.key(node.data):
            return self._search(node.left, goal)
        return self._search(node.right, goal)

    def delete(self, goal: Any):
        self.root = self._delete(self.root, goal)
        self._size -= 1

    def _delete(self, node: Node, goal: Any) -> Node | None:
        # If the node is None, we return None
        if node is None:
            return node

        # If the goal is less than the node data, we go to the left
        if self.key(goal) < self.key(node.data):
            node.left = self._delete(node.left, goal)
        # If the goal is greater than the node data, we go to the right
        elif self.key(goal) > self.key(node.data):
            node.right = self._delete(node.right, goal)
        # If the goal is equal to the node data, we delete the node
        else:
            # If the node has only one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # If the node has two children
            # We get the minimum value of the right subtree
            node.data = self._min_value(node.right)
            node.right = self._delete(node.right, node.data)
        return node

    @staticmethod
    def _min_value(node: Node) -> T:
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def is_empty(self) -> bool:
        return self.root is None

    def __len__(self) -> int:
        return self._size

    @property
    def height(self) -> int:
        if self.root is None:
            return 0

        return self._height(self.root)

    def _height(self, node: Node) -> int:
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def __str__(self) -> str:
        """
        Returns a string representation of the tree that can be printed to console as a hierarchy horizontally
        """
        if self.root is None:
            return "Empty tree"
        return self._print(self.root, 0)

    def _print(self, node: Node, level: int) -> str:
        if node is None:
            return ""
        result = ""
        result += self._print(node.right, level + 1)
        result += "\n" + "    " * level + str(node.data)
        result += self._print(node.left, level + 1)
        return result