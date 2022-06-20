from typing import *
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = -math.inf
        ans = None

        for value, freq in counter.items():
            if freq > max_freq:
                max_freq = freq
                ans = value

        return ans


test_case = [3, 2, 3]
s = Solution()
majority_element = s.majorityElement(test_case)
print(majority_element)
