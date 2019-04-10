class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_val = l1.val + l2.val
        prev_val = 0
        if sum_val > 9:
            prev_val = 1
            sum_val = sum_val % 10

        l1 = l1.next
        l2 = l2.next

        first_node = ListNode(sum_val)
        cur_node = first_node
        while l1 != None and l2 != None:
            sum_val = l1.val + l2.val + prev_val
            if sum_val > 9:
                prev_val = 1
                sum_val = sum_val % 10
            else:
                prev_val = 0

            cur_node.next = ListNode(sum_val)
            cur_node = cur_node.next

            l1 = l1.next
            l2 = l2.next

        remain_node = l1 or l2

        while remain_node != None:
            sum_val = remain_node.val + prev_val
            if sum_val > 9:
                prev_val = 1
                sum_val = sum_val % 10
            else:
                prev_val = 0

            cur_node.next = ListNode(sum_val)
            cur_node = cur_node.next

            remain_node = remain_node.next

        if prev_val:
            cur_node.next = ListNode(prev_val)
            cur_node = cur_node.next

        return first_node