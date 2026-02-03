# LeetCode 3637
# Problem: Trionic Array I
# Link: https://leetcode.com/problems/trionic-array-i/
#
# Approach:
# A trionic array must follow exactly three phases:
# 1) Strictly increasing
# 2) Strictly decreasing
# 3) Strictly increasing
#
# We scan the array once from left to right and simulate these phases.
# Each phase must contain at least one valid comparison, and all comparisons
# must be strict (no equal adjacent elements allowed).
#
# If the array successfully completes all three phases and reaches the end,
# it is a valid trionic array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isTrionic(self, nums: List[int]) -> bool: # type: ignore
        n = len(nums)
        i = 1

        # Phase 1: strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False

        # Phase 2: strictly decreasing
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        if i == n:
            return False

        # Phase 3: strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1

        return i == n
