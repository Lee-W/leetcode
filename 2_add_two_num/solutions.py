class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev_val, sum_val = divmod(l1.val + l2.val, 10)
        l1, l2 = l1.next, l2.next

        first_node = ListNode(sum_val)
        cur_node = first_node
        while l1 is not None and l2 is not None:
            prev_val, sum_val = divmod(l1.val + l2.val + prev_val, 10)
            l1, l2 = l1.next, l2.next

            cur_node.next = ListNode(sum_val)
            cur_node = cur_node.next

        remain_node = l1 or l2
        while remain_node is not None:
            prev_val, sum_val = divmod(remain_node.val + prev_val, 10)
            remain_node = remain_node.next

            cur_node.next = ListNode(sum_val)
            cur_node = cur_node.next

        if prev_val:
            cur_node.next = ListNode(prev_val)
            cur_node = cur_node.next

        return first_node
