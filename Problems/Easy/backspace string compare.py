import itertools

class Solution:
    # my solution in O(n) time O(n) space
    def backspaceCompare(self, s: str, t: str) -> bool:
        # i = j = 0
        # result_s = ""
        # result_t = ""
        # while i < len(s):
        #     if s[i] != "#":
        #         result_s += s[i]
        #     elif s[i] == "#" and result_s:
        #         result_s = result_s[:-1]
        #     i+=1
        #
        # while j < len(t):
        #
        #     if t[j] != "#":
        #         result_t += t[j]
        #     elif t[j] == "#" and result_t:
        #         result_t = result_t[:-1]
        #     j+=1
        #
        # return result_s == result_t

        # leetcode solution in O(n) time O(1) space
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        xyz = itertools.zip_longest(F(s), F(t))

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))


test_s = "ab#c"
test_t = "ab#cd"

s = Solution()
print(s.backspaceCompare(test_s, test_t))
