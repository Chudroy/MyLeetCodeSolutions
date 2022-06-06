from typing import *
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)

        left = nums[0:(nums_length // 2)]
        right = nums[(nums_length // 2):]

        if target in left:
            return left.index(target)
        elif target in right:
            return right.index(target) + len(left)

        return -1


test_case = [5]
test_target = 5
solution = Solution()
print(solution.search(test_case, test_target))
