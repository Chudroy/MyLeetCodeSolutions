from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        result = []

        # Append all intervals to result if their upper bound is less than the new interval's lower bound
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # While iterated intervals' lower bound is less than or equal to newInterval's upper bound, update
        # newInterval[0] to the minimum of all the overlapping ranges, and newInterval[1] to the max of all
        # overlapping ranges. This newInterval's upper and lower bound are the minimum and maximum of all overlapping
        # intervals, respectively
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Append newly updated newInterval
        result.append(newInterval)

        # Append all remaining intervals greater than newInterval
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


test_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
test_insert = [4, 8]
s = Solution()
print(s.insert(test_intervals, test_insert))
