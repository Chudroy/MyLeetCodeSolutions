class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

s = Solution()
print(s.hammingWeight(11111111111111111111111111111101))