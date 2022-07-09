class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        ptr1 = 0
        ptr2 = 0
        index_counter = {}
        max_length = 0

        while ptr2 < len(s):
            # if this letter is in the index counter, it's repeated
            # if pointer 1 is less than the index of repeated, jump forward, don't calculate new max length
            if s[ptr2] in index_counter and ptr1 <= index_counter[s[ptr2]]:
                ptr1 = index_counter[s[ptr2]] + 1
            else:
                max_length = max(max_length, ptr2 - ptr1 + 1)

            index_counter[s[ptr2]] = ptr2
            ptr2 += 1

        return max_length


test_case = "abcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(test_case))

