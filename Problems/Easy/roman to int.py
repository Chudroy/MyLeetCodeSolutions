class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = translations[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if translations[s[i]] >= translations[s[i + 1]]:
                num += translations[s[i]]
            else:
                num -= translations[s[i]]
        return num


s = Solution()
print(s.romanToInt("III"))
