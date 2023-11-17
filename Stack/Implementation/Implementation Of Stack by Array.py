class Stack:
    def __init__(self):
        self.array = []

    def is_empty(self) -> bool:
        return len(self.array) == 0

    def push(self, value: int) -> None:
        self.array.append(value)

    def pop(self):
        if not self.array:
            return -1
        top = self.array[-1]
        self.array.remove(top)
        return top

    def peek(self):
        if not self.array:
            return -1
        return self.array[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)

    while not s.is_empty():
        print(s.peek())
        s.pop()
