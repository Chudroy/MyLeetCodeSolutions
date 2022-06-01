class Solution(object):
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, value in enumerate(nums):
            required_number = target - value
            if required_number in hashmap:
                return [hashmap[reºquired_number], i]

            hashmap[value] = i



nums = [5, 3, 1, 9]
target = 8

solution = Solution.two_sum(nums, target)

print(solution)



