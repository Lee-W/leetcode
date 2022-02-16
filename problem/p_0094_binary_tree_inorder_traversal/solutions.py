from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 39 ms (56.66%)
    Memory Usage: 13.8 MB (99. 3%)
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        cur = root
        stack: List[TreeNode] = []
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result
