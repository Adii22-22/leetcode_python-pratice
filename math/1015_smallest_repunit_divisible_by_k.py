# LeetCode 1015. Smallest Integer Divisible by K
# Solved on Nov 25, 2025
# Pattern: Math / Modular Arithmetic
#
# Approach:
# We cannot construct the number directly since "111...1" grows too large.
# Instead, we simulate the remainder using:
#   remainder = (remainder * 10 + 1) % k
#
# Why this works:
# - Appending a "1" digit mathematically means: new_num = old_num * 10 + 1
# - We only track the remainder, not the full number.
# - A repunit divisible by k must appear within k steps (Pigeonhole Principle).
#
# Special Case:
# If k is divisible by 2 or 5, no repunit can ever be divisible by k → return -1.
#
# Time Complexity: O(k)
# Space Complexity: O(1)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 ==0:
            return -1
        reminder = 0
        length = 0
        for i in range(1,k+1):
            reminder = (reminder * 10 + 1) % k
            if reminder == 0:
                return i
        return -1
        