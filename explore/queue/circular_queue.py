class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._size = k
        self._data = [None] * k
        self._rear = -1
        self._front = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self._front = 0
            self._rear = 0
        else:
            self._rear += 1
            self._rear %= self._size
        self._data[self._rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self._data[self._front] = None
        if self._front == self._rear:
            self._front = -1
            self._rear = -1
        else:
            self._front += 1
            self._front %= self._size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self._data[self._rear]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self._rear == self._front == -1:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self._rear + 1 == self._front or (self._front == 0 and self._rear == self._size - 1):
            return True
        return False
