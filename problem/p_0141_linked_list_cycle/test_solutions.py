import pytest

from .solutions import ListNode, Solution

node_1_1 = ListNode(3)
node_1_2 = ListNode(2)
node_1_3 = ListNode(0)
node_1_4 = ListNode(-4)
node_1_1.next = node_1_2
node_1_2.next = node_1_3
node_1_3.next = node_1_4
node_1_4.next = node_1_2

node_2_1 = ListNode(1)
node_2_2 = ListNode(2)
node_2_1.next = node_2_2
node_2_2.next = node_2_1

node_3_1 = ListNode(1)


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize(
    "value, expected", ((node_1_1, True), (node_2_1, True), (node_3_1, False))
)
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.hasCycle(value) == expected
