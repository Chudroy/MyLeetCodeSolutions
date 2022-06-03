import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pat = re.compile('[^a-zA-Z0-9]+')
        s = re.sub(pat, "", s)
        s = re.sub(" ", "", s)

        for i in range(len(s)):
            print(s[i], s[-i - 1])
            if s[i] != s[-i -1]:
                return False

        return True


# test_case = "a man, a plan, a canal: Panama"
# test_case = "raceacar"
# test_case = ""
test_case = "0P"
s = Solution()
print(s.isPalindrome(test_case))
