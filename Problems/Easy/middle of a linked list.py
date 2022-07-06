from typing import *
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    # O(n) Time complexity O(n) space complexity
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = {}
        list_length = 0
        curr = head

        while curr:
            print(curr.val)
            hash_map[list_length] = curr
            curr = curr.next
            list_length += 1

        if list_length % 2 == 0:
            mid = (list_length / 2) + 1
            return hash_map[int(mid - 1)]

        elif list_length % 2 != 0:
            mid = math.ceil(list_length / 2)
            return hash_map[mid - 1]

        else:
            return None

    # O(n) time complexity O(1) space complexity
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


test_head = ListNode(1)
test_curr = test_head

for i in range(2, 8):
    test_curr.next = ListNode(i)
    test_curr = test_curr.next

s = Solution()
print(s.middleNode(test_head).val)
