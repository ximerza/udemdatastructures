class ArrayQueue[T]:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data: list[T | None] = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size: int = 0
        self._front: int = 0

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def enqueue(self, e: T):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise ValueError('Queue is empty')
        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return e

    def first(self) -> T:
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._data[self._front]

    def _resize(self, capacity: int):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
