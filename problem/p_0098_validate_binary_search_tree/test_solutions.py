import pytest

from .solutions import Solution, Solution2, TreeNode

tree_node_3 = TreeNode(3, None, None)
tree_node_2 = TreeNode(2, tree_node_3, None)
tree_node_1 = TreeNode(1, None, tree_node_2)


@pytest.mark.parametrize("solution_cls", [Solution, Solution2])
@pytest.mark.parametrize("value, expected", ((tree_node_1, False),))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.isValidBST(value) == expected
