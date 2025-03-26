from typing import Any

class Node[T]:

    def __init__(self, data:T):
        self.data: T = data
        self.left: Node | None = None
        self.right: Node | None = None

class BinarySearchTree[T]:

    def __init__(self, root: Node |None = None, key=lambda x: x):
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
        if self.key(data) < self.key(node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right,data)

    def delete(self, goal: Any):
        self.root = self._delete(self.root,goal)
        #ToDo: verificar que si se encontró el elemento
        self._size -=1

    def _delete(self, node: Node, goal: Any):
        if node is None:
            return node

        if self.key(goal) < self.key(node.data):
            node.left = self._delete(node.left, goal)
        elif self.key(goal) > self.key(node.data):
            node.right = self._delete(node.right, goal)
        else:
            if node.left is None:
                return node.left

            if node.right is None:
                return node.left


            node.data = self._min_value(node.right)
            node.right = self._delete(node.right, node.data)
        return node

    def _min_value(self, node: Node) -> T:
        current = node
        while current.left is not None:
            current = current.left
        return

    def __str__(self) -> str:
        if self.root is None:
            return "Empty tree"
        return self._print(self.root, 0)


    def _print(self, node: Node, level: int):
        if node is None:
            return ""
        result = ""
        result += self._print(node.right, level + 1)
        result += "\n" + "   " * level + str(node.data)
        result += self._print(node.left, level +1)
        return result
