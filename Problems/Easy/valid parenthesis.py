class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")": "(",
                   "}": "{",
                   "]": "["}

        opening = set('([{')
        closing = set(')]}')

        stack = []

        for i, val in enumerate(s):

            print(stack)

            if val in hashmap:
                if not stack:
                    return False
                else:
                    if hashmap[val] == stack.pop():
                        continue
                    else:
                        return False
            else:
                stack.append(val)

        print("stack at the end of the loop: ", stack)


test_string = "{{{{{{{{{{}}}}}}}}}}"
Solution.isValid(Solution, test_string)
