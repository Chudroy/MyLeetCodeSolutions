class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # n-1
        n_minus_1 = 2
        # n-2
        n_minus_2 = 1
        # total combinations
        all_ways = 0

        for _ in range(2, n):
            print(n_minus_1, n_minus_2)
            all_ways = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = all_ways

        return all_ways


s = Solution()
print(s.climbStairs(5))
