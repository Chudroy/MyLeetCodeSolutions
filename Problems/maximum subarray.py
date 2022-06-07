from typing import *
from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_maximum = 0
        global_maximum = -inf

        for i in range(len(nums)):
            local_maximum = max(nums[i], nums[i] + local_maximum)

            if local_maximum > global_maximum:
                global_maximum = local_maximum

        return global_maximum


nums = [-1]

s = Solution()
print(s.maxSubArray(nums))
