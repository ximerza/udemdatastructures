from collections.abc import Callable
from typing import Any

LIST_IS_EMPTY = "List is empty"


class Node[T]:
    """
    Node class for SinglyLinkedList

    Attributes:
    data: T
        The data to be stored in the node
    next: Node[T] | None
        The next node in the linked list
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] | None = None


class SinglyLinkedList[T]:
    """
    SinglyLinkedList class

    Attributes:
    head: Node[T] | None
        The head of the linked list

    """
    def __init__(self):
        """
        Initialize an empty linked list
        """
        self.head: Node[T] | None = None

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty
        :return: bool - True if the linked list is empty, False otherwise
        """
        return self.head is None

    def insert(self, data: T) -> None:
        """
        Insert a new node at the beginning of the linked list
        :param data: T - The data to be stored in the new node
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = lambda x: x) -> None:
        """
        Insert a new node after a node with a specific key
        :param new_data: The data to be stored in the new node
        :param goal: The key to search for
        :param key: The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(LIST_IS_EMPTY)
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise KeyError("Key not found")

    def append(self, data: T) -> None:
        """
        Append a new node at the end of the linked list

        :param data: T - The data to be stored in the new node
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self) -> None:
        """
        Reverse the linked list in place

        :raises ValueError: If the linked list is empty
        """
        if self.is_empty():
            raise ValueError(LIST_IS_EMPTY)
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = lambda x: x) -> Node[T] | None:
        """
        Find the first node with a specific key

        :param goal: The key to search for
        :param key: The function to extract the key from the data. Default is the identity function
        :return: Node[T] | None - The node with the key or None if not found
        """
        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            current = current.next
        return None

    def __contains__(self, item: Any) -> bool:
        """
        Check if the linked list contains a specific item
        :param item:  The item to search for
        :return:  bool - True if the item is found, False otherwise
        """
        return self.find(item) is not None

    def delete(self, goal: Any, key: Callable[[T], Any] = lambda x: x) -> None:
        """
        Delete the first node with a specific key

        :param goal:  The key to search for
        :param key:  The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(LIST_IS_EMPTY)

        if key(self.head.data) == goal:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        while current:
            if key(current.data) == goal:
                previous.next = current.next
                return
            previous = current
            current = current.next

        raise KeyError("Key not found")

    def clear(self) -> None:
        """
        Clear the linked list
        """
        self.head = None

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        return f"LinkedList([{', '.join(repr(data) for data in self)}])"

    def __str__(self) -> str:
        return " -> ".join(str(data) for data in self)
