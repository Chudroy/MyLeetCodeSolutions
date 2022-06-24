import copy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            temp_rev = rev
            rev = copy.copy(slow)
            rev.next = temp_rev
            slow = slow.next

            # rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True


test_head = ListNode(1)
test_head.next = ListNode(2)
test_head.next.next = ListNode(3)
test_head.next.next.next = ListNode(4)
test_head.next.next.next.next = ListNode(2)
test_head.next.next.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(test_head))

