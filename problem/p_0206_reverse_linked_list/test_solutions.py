import pytest

from .solutions import ListNode, Solution

node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", ((node_1, [5, 4, 3, 2, 1]), (None, None)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()

    new_head = solution.reverseList(value)
    if new_head:
        results = [new_head.val]
        while new_head.next:
            new_head = new_head.next
            results.append(new_head.val)
        assert results == expected
    else:
        assert new_head == expected
