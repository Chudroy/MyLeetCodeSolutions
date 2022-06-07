from typing import *


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.color, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, new_data: int):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = dummy = ListNode(0)

        while True:
            if list1 is None:
                cur.next = list2
                break
            elif list2 is None:
                cur.next = list1
                break

            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next

            cur = cur.next

        return dummy.next


list_a = LinkedList()

list_a.addToList(1)
list_a.addToList(2)
list_a.addToList(3)
list_a.addToList(4)

list_b = LinkedList()

list_b.addToList(1)
list_b.addToList(2)
list_b.addToList(4)
list_b.addToList(5)

s = Solution()

mergedList = LinkedList()
mergedList.head = s.mergeTwoLists(list_a.head, list_b.head)

mergedList.printList()
