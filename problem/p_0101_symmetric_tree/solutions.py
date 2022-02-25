# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 36 ms (83.98 %)
    Memory Usage: 14.1 MB (66.51 %)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        if not (root.left or root.right):
            return True

        if not (root.left and root.right):
            return False

        pre_level = [root]
        cur_level = []
        while pre_level:
            cur = pre_level.pop(0)

            if cur.left:
                cur_level.append(cur.left)

            if cur.right:
                cur_level.append(cur.right)

            if not pre_level:
                cur_length = len(cur_level)
                if cur_length % 2:
                    return False

                for i in range(cur_length // 2):
                    left = cur_level[i]
                    right = cur_level[cur_length - i - 1]

                    if left.val != right.val:
                        return False

                    if left.left and (
                        not right.right or (left.left.val != right.right.val)
                    ):
                        return False

                    if left.right and (
                        not right.left or (left.right.val != right.left.val)
                    ):
                        return False

                pre_level = cur_level
                cur_level = []
        return True


class Solution2:
    """
    Runtime: 28 ms (98.24 %)
    Memory Usage: 13.9 MB (84.36 %)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.are_trees_symmetric(root.left, root.right)

    def are_trees_symmetric(self, left: TreeNode, right: TreeNode):
        if left and right and left.val == right.val:
            return self.are_trees_symmetric(
                left.left, right.right
            ) and self.are_trees_symmetric(left.right, right.left)

        return left == right
