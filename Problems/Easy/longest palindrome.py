from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = set()

        for letter in s:

            if letter in odds:
                odds.remove(letter)
            else:
                odds.add(letter)

        return len(s) - len(odds) + bool(odds)



test_case = "abccccdd"
s = Solution()
print(s.longestPalindrome(test_case))