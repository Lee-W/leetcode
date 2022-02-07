import pytest

from .solutions import ListNode, Solution

node_1_4 = ListNode(1)
node_1_3 = ListNode(2, node_1_4)
node_1_2 = ListNode(2, node_1_3)
node_1_1 = ListNode(1, node_1_2)


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", ((node_1_1, True),))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.isPalindrome(value) == expected
