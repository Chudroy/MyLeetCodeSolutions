from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, copy, visited: List):
        # [0, 1, 2, ... copy.val, ...]
        visited[copy.val] = copy

        for n in node.neighbors:
            if not visited[n.val]:
                c = Node(n.val)
                copy.neighbors.append(c)
                self.dfs(n, c, visited)
            else:
                copy.neighbors.append(visited[n.val])

    def cloneGraph(self, node: Node) -> Node:
        copy = Node(node.val)
        visited = [None] * 101
        self.dfs(node, copy, visited)
        return copy


