from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            adj_list[x].append(y)

        for i in range(numCourses):
            if not self.dfs(i, visited, adj_list):
                return False

        return True

    def dfs(self, i, visited, adj_list):
        if visited[i] == -1:
            return False

        if visited[i] == 1:
            return True

        visited[i] = -1
        for j in adj_list[i]:
            if not self.dfs(j, visited, adj_list):
                return False
        visited[i] = 1
        return True


test_case = [[0, 5], [1, 0], [2, 1], [3, 1]]
s = Solution()
print(s.canFinish(6, test_case))
