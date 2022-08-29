from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "/":
                    print(l, r, l / r)
                    stack.append(int(l // r))
                elif t == "*":
                    stack.append(l * r)

        return stack.pop()


test_case = ["4", "13", "5", "/", "+"]
s = Solution()
print(s.evalRPN(test_case))

list = [[x for x in range(3)] for y in range(3)]
print(list)