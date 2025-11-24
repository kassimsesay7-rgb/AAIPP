class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

# Test example
if __name__ == "__main__":
    s = Stack()
    s.push('1')
    s.push('2')
    s.push('3')
    print("After pushing: '1', '2', '3'")
    print("Peek:", s.peek())  # Should print '3'
    print("Pop:", s.pop())    # Should remove and print '3'
    print("Peek after pop:", s.peek())  # Should print '2'
