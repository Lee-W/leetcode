class MyStack:
    """
    Runtime: 32 ms (72.51 %)
    Memory Usage: 14 MB (92.31 %)
    """

    def __init__(self):
        self.queue = []
        self.top_value = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_value = x

    def pop(self) -> int:
        tmp_queue = []
        while self.queue[:-2]:
            tmp_queue.append(self.queue.pop(0))

        sec_top = self.queue.pop(0)
        if self.queue:

            self.top_value = sec_top
            tmp_queue.append(sec_top)
            top_value = self.queue.pop(0)
        else:
            top_value = sec_top
            self.top_value = None

        self.queue = tmp_queue
        return top_value

    def top(self) -> int:
        return self.top_value

    def empty(self) -> bool:
        return not bool(self.queue)
