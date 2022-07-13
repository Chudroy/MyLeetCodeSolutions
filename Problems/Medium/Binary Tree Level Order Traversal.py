from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        ans = []
        queue = [root]

        while queue:
            level_length = len(queue)
            sub_list = []

            for i in range(level_length):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                sub_list.append(current.val)

            ans.append(sub_list)

        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

s = Solution()
print(s.levelOrder(root))

test = {"a": 1, "b": 2, "c": 3}


def convertir_a_lista(input_dictionary):
    k_list = []
    v_list = []
    for k, v in input_dictionary.items():
        k_list.append(k)
        v_list.append(v)
    return k_list, v_list


a, b = convertir_a_lista(test)
print(a)
print(b)

a = [list(k) for k in test.items()]
print(a)

# [1,2,null,3,null,4,null,5]
