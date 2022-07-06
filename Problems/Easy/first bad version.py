from math import *

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n

        while low < high:
            mid = low + floor((high - low) / 2)

            if isBadVersion(mid):
                high = mid
            elif not isBadVersion(mid):
                low = mid + 1

        return low
