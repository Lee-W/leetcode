# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

        if not l2:
            return l1
