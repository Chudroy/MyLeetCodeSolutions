from collections import defaultdict


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = dict.fromkeys(range(len(nums)+1), 0)

        for i in range(len(nums) + 1):
            counter[i] = 0

        for i in range(len(nums)):
            counter[nums[i]] += 1

        return list(counter.keys())[list(counter.values()).index(0)]


test_case = [3, 0, 1]
s = Solution()
print(s.missingNumber(test_case))
