from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def find_rightmost(node: TreeNode) -> TreeNode:
        rightmost = node
        while rightmost.right:
            rightmost = rightmost.right
        return rightmost

    @staticmethod
    def find_leftmost(node: TreeNode) -> TreeNode:
        leftmost = node
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 44 ms (95.53 %)
        Memory Usage: 17.1 MB (15.56 %)
        """

        if not root or not (root.left or root.right):
            return True

        if root.left and root.right:
            if self.isValidBST(root.left) and self.isValidBST(root.right):
                rightmost_left = self.find_rightmost(root.left)
                leftmost_right = self.find_leftmost(root.right)
                if rightmost_left.val < root.val < leftmost_right.val:
                    return True
            return False

        if root.left:
            if self.isValidBST(root.left):
                rightmost_left = self.find_rightmost(root.left)
                if rightmost_left.val < root.val:
                    return True
            return False

        if root.right:
            if self.isValidBST(root.right):
                leftmost_right = self.find_leftmost(root.right)
                if root.val < leftmost_right.val:
                    return True
            return False

        return False


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 44 ms (93.53 %)
        Memory Usage: 16.7 MB (28.08 %)
        """

        def validate(node, left_val, right_val):
            if not node:
                return True

            if not (left_val < node.val < right_val):
                return False

            return validate(node.left, left_val, node.val) and validate(
                node.right, node.val, right_val
            )

        return validate(root, -float("inf"), float("inf"))
