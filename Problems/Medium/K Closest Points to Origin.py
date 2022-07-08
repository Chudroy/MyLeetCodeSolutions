from typing import *
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        priority_queue = []

        for x, y in points:
            dist = -(x * x + y * y)
            if len(priority_queue) == k:
                heapq.heappushpop(priority_queue, (dist, x, y))
            else:
                heapq.heappush(priority_queue, (dist, x, y))

        return [(x, y) for (dist, x, y) in priority_queue]


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))