class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init(self):
        self.h = 0


def diameterOpt(root, height):
    
    lh = Height()
    rh = Height()

    if root is None:
        height.h = 0
        return 0

    left_diameter = diameterOpt(root.left, lh)
    right_diameter = diameterOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    '''
    return the diameter. diameter of a node can be the maximum 
    value between the left or right sub-tree's diameter, 
    or the sum of left and right  sub-tree's height
    '''

    return max(lh.h + rh.h, max(left_diameter, right_diameter))



def diameter(root):
    height = Height()
    return diameterOpt(root, height)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""

print(diameter(root))
