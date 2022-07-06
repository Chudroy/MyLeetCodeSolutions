class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[::-1] != x:
            return False
        return True


test_case = 12321
s = Solution()
print(s.isPalindrome(test_case))
