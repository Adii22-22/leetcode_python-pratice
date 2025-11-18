# ------------------------------------------------------------
# LeetCode 155: Min Stack
# Difficulty: Medium
# Date Solved: Nov 16, 2025
#
# Approach:
# - Use two stacks:
#     1. `stack` for storing all values.
#     2. `min_stack` for storing the minimum value at each level.
#
# - When pushing a value:
#       • Always push it to the main stack.
#       • For min_stack: push either the value itself (if empty)
#         or the minimum between this value and the previous
#         minimum (min_stack[-1]).
#
# - When popping:
#       • Pop from both stacks to keep them synchronized.
#
# - `top()` simply returns the top of the main stack.
# - `getMin()` returns the top of min_stack, which always holds
#   the current minimum of the entire stack.
#
# Key Insight:
# - By storing running minimums in `min_stack`, retrieving the
#   minimum becomes O(1). No scanning or recomputation needed.
#
# Time Complexity:
#   • push()   -> O(1)
#   • pop()    -> O(1)
#   • top()    -> O(1)
#   • getMin() -> O(1)
#
# Space Complexity: O(n) due to using two stacks
# ------------------------------------------------------------
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()