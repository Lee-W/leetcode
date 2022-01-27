class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 816 ms (72.27 %)
    Memory Usage: 39.5 MB (64.29 %)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        if length == 1:
            return True

        first_node, second_node = head, head.next
        for _ in range(length // 2 - 1):
            first_node.next = second_node.next
            second_node.next = head
            head, second_node = second_node, first_node.next

        if length % 2:
            second_node = second_node.next

        while head and second_node:
            if head.val != second_node.val:
                return False
            head = head.next
            second_node = second_node.next

        return True
