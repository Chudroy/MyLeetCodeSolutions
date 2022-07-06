class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_num = 0
        for i in range(32):
            # if n is smaller than
            if n & (1 << i):
                reverse_num |= 1 << (31 - i)

        return reverse_num


test_case = int("01111111111111111111111110110110", 2)
s = Solution()
ans = s.reverseBits(test_case)

for i in range(32):
    print(test_case & (1 << i))
    print(bin(test_case), "|||", bin(1 << i))
    print(bin(test_case & (1 << i)))
