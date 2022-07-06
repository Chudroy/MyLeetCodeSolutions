from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root is None:
                return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


'''
                0
             /     \
            1       2
          / \      / \ 
         3   4    5   6
'''

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

s = Solution()
print(s.maxDepth(root))