import pytest

from .solutions import Solution, TreeNode

tree_node_3 = TreeNode(3, None, None)
tree_node_2 = TreeNode(2, None, None)
tree_node_1 = TreeNode(1, tree_node_2, tree_node_3)
# [1,2,3], targetSum = 5


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", ((((tree_node_1, 5), False)),))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.hasPathSum(*value) == expected
