from collections.abc import Callable
from typing import Any, override


_KEY_NOT_FOUND = "Key not found"
_LIST_IS_EMPTY = "List is empty"


def _identity(x: Any) -> Any:
    return x


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

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = _identity) -> None:
        """
        Insert a new node after a node with a specific key
        :param new_data: The data to be stored in the new node
        :param goal: The key to search for
        :param key: The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

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
            raise ValueError(_LIST_IS_EMPTY)
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = _identity) -> Node[T] | None:
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

    def delete(self, goal: Any, key: Callable[[T], Any] = _identity) -> None:
        """
        Delete the first node with a specific key

        :param goal:  The key to search for
        :param key:  The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)

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

        raise KeyError(_KEY_NOT_FOUND)

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
        return f"SinglyLinkedList([{', '.join(repr(data) for data in self)}])"

    def __str__(self) -> str:
        return " -> ".join(str(data) for data in self)


class OrderedLinkedList[T](SinglyLinkedList):
    """
    OrderedLinkedList class

    The OrderedLinkedList class is a subclass of SinglyLinkedList that maintains the elements in sorted order.

    Attributes:
    key: Callable[[Any], Any]
        The function to extract the key from the data. Default is the identity function
    """
    def __init__(self, key: Callable[[Any], Any] = _identity):
        super().__init__()
        self.key: Callable[[Any], Any] = key

    @override
    def insert(self, data: T) -> None:
        """
        Insert a new node in sorted order

        :param data: T - The data to be stored in the new node
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        if self.key(self.head.data) > self.key(data):
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if self.key(current.next.data) > self.key(data):
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node

    @override
    def find(self, goal: Any, key: Callable[[T], Any] = _identity) -> Node[T] | None:
        return super().find(goal, self.key)

    @override
    def delete(self, goal: Any, key: Callable[[T], Any] = _identity):
        super().delete(goal, self.key)

    @override
    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = _identity):
        raise NotImplementedError("insert_at is not supported for OrderedLinkedList")

    @override
    def reverse(self):
        raise NotImplementedError("reverse is not supported for OrderedLinkedList")

    @override
    def append(self, data: T):
        raise NotImplementedError("append is not supported for OrderedLinkedList")

    def __repr__(self):
        return f"OrderedLinkedList([{', '.join(repr(data) for data in self)}])"


class DoubleEndedLinkedList[T](SinglyLinkedList):
    """
    DoubleEndedLinkedList class

    The DoubleEndedLinkedList class is a subclass of SinglyLinkedList that maintains a reference to the tail of the
    linked list.

    Attributes:
    tail: Node[T] | None
        The tail of the linked list
    """
    def __init__(self):
        super().__init__()
        self.tail: Node[T] | None = None

    @override
    def insert(self, data: T) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    @override
    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    @override
    def delete(self, goal: Any, key: Callable[[Any], Any] = _identity) -> None:
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        if key(self.head.data) == goal:
            self.head = self.head.next
            return

        current = self.head.next
        previous = self.head
        while current:
            if key(current.data) == goal:
                if current == self.tail:
                    self.tail = previous
                previous.next = current.next
                return
            previous = current
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

    @override
    def reverse(self):
        super().reverse()
        self.head, self.tail = self.tail, self.head


class CircularLinkedList[T](DoubleEndedLinkedList[T]):
    """
    CircularLinkedList class

    The CircularLinkedList class is a subclass of DoubleEndedLinkedList that maintains a reference to the tail of the
    linked list.
    """

    def __init__(self):
        super().__init__()

    @override
    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            return

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    @override
    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = _identity) -> None:
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)

        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            if current == self.tail:
                raise KeyError(_KEY_NOT_FOUND)
            current = current.next

    @override
    def find(self, goal: Any, key: Callable[[T], Any] = _identity) -> Node[T] | None:
        if self.is_empty():
            return None

        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            if current == self.tail:
                return None
            current = current.next

    @override
    def __len__(self):
        if self.is_empty():
            return 0

        count = 1
        current = self.head
        while current != self.tail:
            count += 1
            current = current.next
        return count

    @override
    def __iter__(self):
        if self.is_empty():
            return

        current = self.head
        while current != self.tail:
            yield current.data
            current = current.next
        yield self.tail.data


class DoublyNode[T]:
    """
    DoublyNode class
    
    Node class for DoublyLinkedList
    
    Attributes:
    data: T
        The data to be stored in the node
    next: DoublyNode[T] | None
        The next node in the linked list
    prev: DoublyNode[T] | None
        The previous node in the linked list
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: DoublyNode[T] | None = None
        self.prev: DoublyNode[T] | None = None


class DoublyLinkedList[T]:
    """
    DoublyLinkedList class
    
    Attributes:
    head: DoublyNode[T] | None
        The head of the linked list
    """
    def __init__(self):
        self.head: DoublyNode[T] | None = None

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty
        Returns: bool - True if the linked list is empty, False otherwise
        """
        return self.head is None

    def insert(self, data: T) -> None:
        """
        Insert a new node at the beginning of the linked list
        
        :param data: T - The data to be stored in the new node 
        """
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = _identity) -> None:
        """
        Insert a new node after a node with a specific key

        :param new_data: T - The data to be stored in the new node
        :param goal: Any - The key to search for
        :param key: Callable[[Any], Any] - The function to extract the key from the data. Default is the identity
            function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = DoublyNode(new_data)
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

    def append(self, data: T) -> None:
        """
        Append a new node at the end of the linked list

        :param data: T - The data to be stored in the new node
        """
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def reverse(self) -> None:
        """
        Reverse the linked list in place

        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = _identity) -> DoublyNode[T] | None:
        """
        Find the first node with a specific key

        :param goal: Any - The key to search for
        :param key: Callable[[T], Any] - The function to extract the key from the data. Default is the identity function

        :return: DoublyNode[T] | None - The node with the key or None if not found
        """
        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            current = current.next
        return None

    def delete(self, goal: Any, key: Callable[[T], Any] = _identity) -> None:
        """
        Delete the first node with a specific key

        :param goal: Any - The key to search for
        :param key: Callable[[T], Any] - The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        if key(self.head.data) == goal:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if key(current.next.data) == goal:
                current.next = current.next.next
                return
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

    def clear(self) -> None:
        """
        Clear the linked list
        """
        self.head = None

    def __contains__(self, item: Any) -> bool:
        """
        Check if the linked list contains a specific item

        :param item: Any - The item to search for

        :return: bool - True if the item is found, False otherwise
        """
        return self.find(item) is not None

    def __len__(self):
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

    def __str__(self) -> str:
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return " <-> ".join(map(str, result))

    def __repr__(self) -> str:
        return f"DoublyLinkedList([{', '.join(repr(data) for data in self)}])"
