class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")": "(",
                   "}": "{",
                   "]": "["}

        stack = [len(s)]
        for i, val in enumerate(s):

            print(i)
            print(val in hashmap)

            if hashmap:
                print(hashmap[val] == stack[i - 1])

            if i != 0 and val in hashmap and hashmap[val] == stack[i - 1]:
                stack.pop()

            stack.append(val)


test_string = "{{}[][[[]]]}"
Solution.isValid(Solution, test_string)
