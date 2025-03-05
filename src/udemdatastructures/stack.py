class ArrayStack[T]:

    def __init__(self):
        self._data: list[T] = []

    def __len__(self):
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, e: T):
        self._data.append(e)

    def top(self) -> T:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    def pop(self) -> T:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()