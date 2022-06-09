from typing import *


class MyQueue:

    def __init__(self):
        self.push_stack: List = []
        self.pop_stack: List = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            self.transfer_stack(self.push_stack, self.pop_stack)
        return self.pop_stack.pop()

    def peek(self) -> int:
        if not self.pop_stack:
            self.transfer_stack(self.push_stack, self.pop_stack)
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def transfer_stack(self, from_stack: List, to_stack: List):
        for i in range(len(from_stack)):
            val = from_stack.pop()
            to_stack.append(val)

# my_queue = MyQueue()
# my_queue.push(1)
# my_queue.push(2)
# my_queue.push(3)
# my_queue.push(4)
# my_queue.push(5)
#
# print("push stack: ", my_queue.push_stack)
# print("pop stack: ", my_queue.pop_stack)
#
# print("popping first element in: ", my_queue.pop())
#
# print("push stack: ", my_queue.push_stack)
# print("pop stack: ", my_queue.pop_stack)
#
# my_queue.push(6)
# my_queue.push(7)
# my_queue.push(8)
# my_queue.push(9)
#
# print("push stack: ", my_queue.push_stack)
# print("pop stack: ", my_queue.pop_stack)
#
# my_queue.pop()
# my_queue.pop()
# my_queue.pop()
# my_queue.pop()
# my_queue.pop()
#
#
#
# print("push stack: ", my_queue.push_stack)
# print("pop stack: ", my_queue.pop_stack)
