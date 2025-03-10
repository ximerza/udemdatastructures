class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1])  # Ordena por prioridad

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]  # Retorna el primer elemento (con mayor prioridad)

    def peek(self):
        if not self.is_empty():
            return self.items[0][0]  # Retorna el primer elemento sin removerlo

    def size(self):
        return len(self.items)
