# -------------------------------------------------------------
# LeetCode Problem: 69. Sqrt(x)
# Solved on: Nov 5, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a non-negative integer x, compute and return the square root
# of x truncated to an integer. The returned integer should be the
# floor value of the exact square root.
#
# Example:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.828..., and since we must
# return the integer part only, the answer is 2.
#
# Approach:
# Use binary search to find the integer square root:
# - Initialize two pointers: low = 0, high = x
# - Repeatedly find mid = (low + high) // 2
# - If mid² <= x, move the lower bound up (low = mid + 1)
# - Otherwise, move the upper bound down (high = mid - 1)
# - When the loop ends, 'high' will hold the integer square root.
#
# Time Complexity: O(log x)
# Space Complexity: O(1)
# -------------------------------------------------------------

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high
