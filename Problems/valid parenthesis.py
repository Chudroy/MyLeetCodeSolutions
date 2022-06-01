class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")": "(",
                   "}": "{",
                   "]": "["}

        stack = []

        for i, val in enumerate(s):

            if val in hashmap and i != 0 and stack != []:
                print(i, val, hashmap[val], stack[-1], hashmap[val] == stack[-1])
                pass

            if stack != [] and i != 0 and val in hashmap and hashmap[val] == stack[-1]:
                stack.pop()
            else:
                stack.append(val)

        print(stack == [])


test_string = "{}]"
Solution.isValid(Solution, test_string)
