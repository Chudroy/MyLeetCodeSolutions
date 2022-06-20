class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_result = []

        a_binary = [int(x) for x in a]
        b_binary = [int(y) for y in b]

        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            b_sum = carry

            if i >= 0:
                b_sum += a_binary[i]
            if j >= 0:
                b_sum += b_binary[j]

            i, j = i - 1, j - 1

            carry = 1 if b_sum > 1 else 0

            b_result.append(b_sum % 2)

        if carry:
            b_result.append(carry)

        b_result.reverse()

        return "".join(str(x) for x in b_result)


a = "0111"
b = "1111"

s = Solution()

print(s.addBinary(a, b))

