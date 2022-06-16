from typing import *


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
#
# a.next = b
# b.next = c
# c.next = d
#
# s = Solution()
# reversed_list_head = s.reverseList(a)


