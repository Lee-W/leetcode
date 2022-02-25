from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 36 ms (84.39 %)
    Memory Usage: 14.2 MB (81.21 %)
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []
        while queue:
            tmp_level = [node for node in queue]
            tmp_leval_values = []
            queue = []
            for node in tmp_level:
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                tmp_leval_values.append(node.val)

            result.append(tmp_leval_values)
        return result
