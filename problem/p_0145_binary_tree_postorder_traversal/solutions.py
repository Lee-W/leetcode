from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 28 ms (92.72 %)
    Memory Usage: 13.9 MB (73.82 %)
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, result = [root], []
        while stack:
            cur = stack[-1]
            if not cur.left and not cur.right:
                cur = stack.pop()
                result.append(cur.val)
            else:
                if cur.right:
                    stack.append(cur.right)
                    cur.right = None
                if cur.left:
                    stack.append(cur.left)
                    cur.left = None

        return result
