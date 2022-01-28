class MyQueue:
    """
    Runtime: 28 ms (87.04 %)
    Memory Usage: 14.1 MB (91.08 %)
    """

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmp_stack = []
        while self.stack:
            tmp_stack.append(self.stack.pop())

        front = tmp_stack.pop()
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

        return front

    def peek(self) -> int:
        tmp_stack = []
        while self.stack:
            tmp_stack.append(self.stack.pop())

        front = tmp_stack.pop()
        self.stack.append(front)
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

        return front

    def empty(self) -> bool:
        return not bool(self.stack)
