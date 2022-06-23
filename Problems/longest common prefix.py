from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) < 2:
            return strs[0]

        ans = ""
        for i in range(len(strs) - 1):
            pointer = 0
            current_prefix = ""
            while pointer < len(strs[0]) and pointer < len(strs[i + 1]):
                if strs[0][pointer] != strs[i + 1][pointer]:
                    break
                current_prefix += strs[0][pointer]
                pointer += 1
            if not ans:
                if not current_prefix:
                    return current_prefix
                ans = current_prefix
            elif current_prefix < ans:
                ans = current_prefix
        return ans


s = Solution()
print(s.longestCommonPrefix(["c", "acc", "ccc"]))
