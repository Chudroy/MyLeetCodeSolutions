from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def swap(left: Optional[TreeNode], right: Optional[TreeNode]):
    temp = left
    left = right
    right = temp
    return left, right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        stack = []
        queue = [root]

        while queue:

            current_node = queue.pop(0)
            stack.append(current_node)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        while stack:
            current_node = stack.pop()
            current_node.left, current_node.right = swap(current_node.left, current_node.right)

        return root


# Testing stuff
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

inverter = Solution()
inverter.invertTree(root)
#
# cur = root
# stack = []
# queue = []
# tries = 0
#
# queue.append(root)
#
# while queue:
#
#     current_node = queue[0]
#     stack.append(current_node)
#
#     if current_node.left:
#         queue.append(current_node.left)
#     if current_node.right:
#         queue.append(current_node.right)
#
#     queue.pop(0)
#
# while stack:
#     current_node = stack.pop()
#     current_node.left, current_node.right = swap(current_node.left, current_node.right)
#
# print(root.left.left.val)
