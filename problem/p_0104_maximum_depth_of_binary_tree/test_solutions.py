import pytest

from .solutions import Solution, TreeNode

tree_node_7 = TreeNode(7, None, None)
tree_node_15 = TreeNode(15, None, None)
tree_node_20 = TreeNode(20, tree_node_15, tree_node_7)
tree_node_9 = TreeNode(9, None, None)
tree_node_3 = TreeNode(3, tree_node_9, tree_node_20)


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", ((tree_node_3, 3), ([], 0)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.maxDepth(value) == expected
