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
