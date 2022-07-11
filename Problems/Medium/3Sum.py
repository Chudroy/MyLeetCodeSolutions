from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            front = i + 1
            back = len(nums) - 1

            while front < back:
                current_sum = nums[front] + nums[back]

                if current_sum < target:
                    front += 1
                elif current_sum > target:
                    back -= 1
                else:
                    triplet = [nums[i], nums[front], nums[back]]
                    res.append(triplet)

                    while front < back and nums[front] == triplet[1]:
                        front += 1

                    while front < back and nums[back] == triplet[2]:
                        back -= 1
        print(nums)
        return res


test_case = [-2, -1, -1, 0, 1, 1, 2]
s = Solution()
print(s.threeSum(test_case))
