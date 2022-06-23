from typing import *


class Solution:
    def countBits(self, n: int) -> List[int]:
        # number_of_bits(x) = number_of_bits(x/2) if even
        # number_of_bits(x) = number_of_bits((x+1)/2) if odd
        ans = []
        memo = {}

        for i in range(n + 1):
            ans.append(self.number_of_bits(i, memo))

        return ans

    def number_of_bits(self, n, memo):

        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in memo:
            return memo[n]
        elif n % 2 == 0:
            memo[n] = self.number_of_bits(n / 2, memo)
            return memo[n]
        else:
            memo[n] = 1 + self.number_of_bits(int(n / 2), memo)
            return memo[n]


# for i in range(5):
#     print(i, bin(i))

s = Solution()
print(s.countBits(16))
