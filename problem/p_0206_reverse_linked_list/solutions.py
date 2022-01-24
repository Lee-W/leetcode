from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 36 ms (77.44 %)
    Memory Usage:  15.5 MB (77.44 %)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        first_node, second_node = head, head.next
        while first_node and second_node:
            first_node.next = second_node.next
            second_node.next = head

            head, second_node = second_node, first_node.next

        return head
