from typing import *
import math
from collections import deque


class Solution:
    def updateMatrixDP(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Iterate from top left to bottom right, calculating the min distance from a 0 of top and right neighbours
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        # Iterate from bottom right to top left, calculating the min distance from 0 of bottom and right neighbours
        for r in range(m - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat

    def updateMatrixBFS(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        # Append all 0's to a list, and assign all other values to -1 to mark as unprocessed
        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1

        # Pop from queue and calculate distance from 0 of all neighbours.
        # Newly calculated neighbours are added to the queue
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))

        return mat


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
s = Solution()
print(s.updateMatrixDP(mat))
