from typing import *


class Node:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.color = val


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:

        # weird AF gotcha, if the new color is the same as the starting node's color,
        # and the starting node is next to another node with the same color.
        # they indefinitely add each other as neighbours to visit.

        # solution: if you want to flood fill at a starting node that is already the same colour as the new colour,
        # just return the image as is.

        if image[sr][sc] == new_color:
            return image

        old_color = image[sr][sc]
        start_node = Node(sr, sc, image[sr][sc])
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if current_node.color == old_color and current_node.i >= 0 and current_node.j >= 0:
                image[current_node.i][current_node.j] = new_color

                try:
                    neighbour_color = image[current_node.i + 1][current_node.j]
                    stack.append(Node(current_node.i + 1, current_node.j, neighbour_color))
                except IndexError:
                    pass
                try:
                    neighbour_color = image[current_node.i - 1][current_node.j]
                    stack.append(Node(current_node.i - 1, current_node.j, neighbour_color))
                except IndexError:
                    pass
                try:
                    neighbour_color = image[current_node.i][current_node.j + 1]
                    stack.append(Node(current_node.i, current_node.j + 1, neighbour_color))
                except IndexError:
                    pass
                try:
                    neighbour_color = image[current_node.i][current_node.j - 1]
                    stack.append(Node(current_node.i, current_node.j - 1, neighbour_color))
                except IndexError:
                    pass

        return image


test_image = [[1, 0, 1], [1, 0, 1], [1, 1, 1]]
test_sr = 1
test_sc = 1
test_newColor = 0

s = Solution()

print(s.floodFill(test_image, test_sr, test_sc, test_newColor))
