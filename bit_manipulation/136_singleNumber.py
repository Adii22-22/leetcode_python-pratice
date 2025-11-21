# 136. Single Number
# Difficulty: Easy
# Solved on: Nov 21, 2025
#
# Approach:
# - Uses XOR to cancel out duplicate numbers.
# - Property: A ^ A = 0, A ^ 0 = A
# - XORing all numbers leaves only the unique (non-duplicate) element.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
