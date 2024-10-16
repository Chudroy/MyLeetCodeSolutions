from typing import *
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, remaining, count):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            if count[remaining - 1] != 0:
                return count[remaining - 1]

            minimum = math.inf

            for coin in coins:
                res = helper(coins, remaining - coin, count)
                print(remaining, coin, remaining-coin, res)
                # assign new minimum
                if 0 <= res < minimum:
                    minimum = 1 + res
                    print("minimum:", minimum)


            count[remaining - 1] = -1 if minimum == math.inf else minimum

            print(count)
            return count[remaining - 1]

        if amount < 1:
            return 0

        return helper(coins, amount, [0] * amount)


s = Solution()

test_coins = [1, 2, 5]

test_amount = 11
print(s.coinChange(test_coins, test_amount))
