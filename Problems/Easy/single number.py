from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            print(xor)
            xor ^= num
            print(num, xor)

        return xor


test_case = [2, 1, 4, 4, 2]
s = Solution()
print(s.singleNumber(test_case))


