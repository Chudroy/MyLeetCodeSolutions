class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


s = Solution()
print(s.hammingWeight(11111111111111111111111111111101))

print(bin(14))
print(bin(13))

a = bin(14)
b = bin(13)
print(10 )
