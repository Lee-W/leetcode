from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 35 ms (98.34 %)
    Memory Usage: 15.1 MB (71.86 %)
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node: TreeNode, cur_sum: int) -> bool:
            new_sum = cur_sum + node.val

            if self.is_leaf(node):
                return new_sum == targetSum

            if node.left and node.right:
                return dfs(node.left, new_sum) or dfs(node.right, new_sum)

            if node.left:
                return dfs(node.left, new_sum)

            return dfs(node.right, new_sum)

        return dfs(root, 0)

    @staticmethod
    def is_leaf(node: TreeNode) -> bool:
        return not (node.left or node.right)
