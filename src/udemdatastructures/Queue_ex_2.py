from src.udemdatastructures.queue import ArrayQueue


def is_symmetric(numbers: list[int]) -> bool:
    queue = ArrayQueue[int]()
    for number in numbers:
        queue.enqueue(number)

    i = -1
    while len(queue) > 1:
        if queue.dequeue() != numbers[i]:
            return  False
        i -= 1

    return True
