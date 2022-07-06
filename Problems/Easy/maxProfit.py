import math
from typing import *
from random import *


# best time to buy and sell stock problem on leetcode
# this works because we have to pointers, "left" and "right, which crawl along the array.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1

        return max_profit


s = Solution()
s.maxProfit(4, 1, 2)
