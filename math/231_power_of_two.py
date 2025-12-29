# LeetCode 231 - Power of Two
# https://leetcode.com/problems/power-of-two/
#
# Approach:
# A number is a power of two if it is positive and has exactly one set bit in binary.
# Using bit manipulation, n & (n - 1) clears the lowest set bit.
# If the result is zero, the number had only one set bit.
#
# Time Complexity: O(1)
# Space Complexity: O(1)
