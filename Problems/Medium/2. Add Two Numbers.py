from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode()
        curr = answer
        carry = 0

        while l1 or l2:
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            sum = num1 + num2

            if sum > 9:
                carry = 1

            curr.next = ListNode((sum % 10) + carry)
            carry = 0
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return answer.next


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

s = Solution()
print(s.addTwoNumbers(l1, l2))
