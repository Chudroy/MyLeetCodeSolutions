from typing import *


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_symmetry(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
        if not left_node and not right_node:
            return left_node == right_node
        elif left_node and right_node:
            return left_node.val == right_node.val \
                   and self.check_symmetry(left_node.left, right_node.right) \
                   and self.check_symmetry(left_node.right, right_node.left)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        return self.check_symmetry(root.left, root.right)
