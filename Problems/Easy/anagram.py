class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = True

        if len(s) != len(t):
            is_anagram = False

        target_dict = {k: t.count(k) for (k) in t}

        for val in s:
            if val in target_dict:
                target_dict[val] -= 1

        for key in target_dict:
            if target_dict[key] != 0:
                is_anagram = False

        return is_anagram


test_string = "anagram"
test_target = "nagaram"

solution = Solution()
print(solution.isAnagram(test_string, test_target))
