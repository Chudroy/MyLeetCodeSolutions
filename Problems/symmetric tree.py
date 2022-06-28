from typing import *


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            if not left_node or not right_node:
                return left_node == right_node

            if left_node.val != right_node.val:
                return False

            outer = check_symmetry(left_node.left, right_node.right)
            inner = check_symmetry(left_node.right, right_node.left)

            return inner and outer

        return check_symmetry(root.left, root.right)
