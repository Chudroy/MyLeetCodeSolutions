from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.helper(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def helper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot
        elif root.val == subRoot.val:
            left = self.helper(root.left, subRoot.left)
            right = self.helper(root.right, subRoot.right)
            return left and right
        return False


root = TreeNode(1)

root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)

# root.right = TreeNode(5)
#
sub_root = TreeNode(1)
# sub_root.left = TreeNode(1)
# sub_root.right = TreeNode(2)

s = Solution()
print(s.isSubtree(root, sub_root))
