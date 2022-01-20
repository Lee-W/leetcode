from typing import Optional


class Node:
    def __init__(self, val: int, next_node: Optional["Node"] = None):
        self.val = val
        self.next_node = next_node

    def __repr__(self) -> str:
        return str(self.val)


class MyLinkedList:
    """
    Runtime: 372 ms (21.8 %)
    Memory Usage: 15.1 MB (29.8 %)
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def get(self, index: int) -> int:
        node = self.head
        while index and node:
            node = node.next_node
            index -= 1

        if not node:
            return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if not index:
            self.addAtHead(val)
            return

        if not self.head:
            return

        node: Optional[Node] = self.head
        while index > 1 and node:
            node = node.next_node
            index -= 1

        if not node:
            return

        new_node = Node(val)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if not index:
            self.head = self.head.next_node
            return

        node: Optional[Node] = self.head
        while index > 1 and node:
            node = node.next_node
            index -= 1

        if not node:
            return

        if node.next_node:
            node.next_node = node.next_node.next_node
