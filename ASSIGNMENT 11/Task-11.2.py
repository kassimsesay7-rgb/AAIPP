from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# Test example
if __name__ == "__main__":
    q = Queue()
    q.enqueue('X')
    q.enqueue('Y')
    q.enqueue('Z')
    print("After enqueue: 'X', 'Y', 'Z'")
    print("Dequeue:", q.dequeue())  # Should remove and print 'X'
    print("Current size:", q.size())  # Should print 2
