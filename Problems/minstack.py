import math


class Node:
    def __init__(self, val, min, next):
        self.val = val
        self.min = min
        self.next = next


class MinStack:

    def __init__(self):
        self.head: Node = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val, None)
        elif self.head:
            self.head = Node(val, min(self.head.min, val), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


# minStack = MinStack()
# minStack.push(-2)
# minStack.push(-1)
# minStack.push(-1)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())

