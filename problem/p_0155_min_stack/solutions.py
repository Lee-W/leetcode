class MinStack:
    """
    Runtime: 60 ms (87.72 %)
    Memory Usage: 18.1 MB (56.64 %)
    """

    def __init__(self):
        self.data = []
        self.min_value = None

    def push(self, val: int) -> None:
        if self.min_value is None or val < self.min_value:
            self.min_value = val
        self.data.append(val)

    def pop(self) -> None:
        if self.min_value == self.data.pop():
            if self.data:
                self.min_value = min(self.data)
            else:
                self.min_value = None

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_value
