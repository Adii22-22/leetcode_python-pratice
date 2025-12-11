# -------------------------------------------------------------
# LeetCode Problem: 303. Range Sum Query - Immutable
# Difficulty: Easy
# Pattern: Prefix Sum
# -------------------------------------------------------------
# Problem Statement:
# Given an integer array 'nums', create a data structure NumArray that
# can return the sum of elements between left and right indices (inclusive).
#
# Example:
# nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
#
# Approach:
# Build a prefix sum array where prefix[i] stores the sum of nums up
# to index i-1. Then the sum of any range [left, right] can be computed
# in O(1) using:
#     prefix[right + 1] - prefix[left]
#
# Time Complexity:
#   - Constructor: O(n)
#   - Query: O(1)
# Space Complexity: O(n)
# -------------------------------------------------------------
class NumArray:
    def __init__(self, nums: List[int]): # type: ignore
        self.nums = nums
        self.prefix = [0]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

        