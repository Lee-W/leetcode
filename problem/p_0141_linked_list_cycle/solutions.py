from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 61 ms (45.65 %)
    Memory Usage: 17.7 MB (57.42 %)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        f_node, s_node = head, head
        while s_node and s_node.next:
            f_node = f_node.next
            s_node = s_node.next.next

            if f_node == s_node:
                return True

        return False
