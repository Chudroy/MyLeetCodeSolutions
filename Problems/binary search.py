from typing import *
from math import *


def recursive_search(arr, l, r, target):
    pass


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left != right:
            mid = left + floor((right - left) / 2)
            print(left, mid, right)
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] == target else -1


test_case = [-5, -1, 0, 1]
test_target =
solution = Solution()
print(solution.search(test_case, test_target))
