from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    Runtime: 57 ms (26.32 %)
    Memory Usage: 14.2 MB (62.14 %)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val <= l2.val:
                first_node = ListNode(l1.val)
                l1 = l1.next
            else:
                first_node = ListNode(l2.val)
                l2 = l2.next

            cur_node = first_node
            while l1 and l2:
                if l1.val <= l2.val:
                    cur_node.next = ListNode(l1.val)
                    cur_node = cur_node.next
                    l1 = l1.next
                else:
                    cur_node.next = ListNode(l2.val)
                    cur_node = cur_node.next
                    l2 = l2.next

            while l1:
                cur_node.next = ListNode(l1.val)
                cur_node = cur_node.next
                l1 = l1.next

            while l2:
                cur_node.next = ListNode(l2.val)
                cur_node = cur_node.next
                l2 = l2.next

            return first_node

        if not l1 and not l2:
            return None

        if not l1:
            return l2
        return l1


class Solution2:
    """
    Runtime: 40 ms (65.91 %)
    Memory Usage:  14.1 MB (85.89 %)
    """

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1

        if list2:
            cur.next = list2

        return head
