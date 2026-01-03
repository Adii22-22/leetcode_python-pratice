# LeetCode 232: Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Approach:
# Use two stacks to simulate queue behavior using only stack operations.
# One stack (in_stack) is used for push operations.
# Another stack (out_stack) is used for pop and peek operations.
#
# When popping or peeking, if out_stack is empty, move all elements from
# in_stack to out_stack. This reverses the order so that the oldest element
# comes to the top of out_stack, preserving FIFO behavior.
#
# Each element is moved at most once between stacks, giving amortized O(1)
# time per operation.
#
# Time Complexity: O(1) amortized per operation
# Space Complexity: O(n)
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
  
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        