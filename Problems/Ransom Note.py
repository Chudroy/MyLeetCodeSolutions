from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)

        return not ransomNote_counter - magazine_counter




ransomNote = "abcq"
magazine = "abcdef"

s = Solution()
print(s.canConstruct(ransomNote, magazine))
