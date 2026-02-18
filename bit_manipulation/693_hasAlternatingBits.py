# LeetCode 693
# Problem: Binary Number with Alternating Bits
# Link: https://leetcode.com/problems/binary-number-with-alternating-bits/
#
# Problem Understanding:
# A number has alternating bits if its binary representation
# contains no two adjacent equal bits.
#
# Example:
# 5  -> 101   -> True
# 7  -> 111   -> False
# 10 -> 1010  -> True
#
# ---------------------------------------------
# Core Trick Used in This Solution:
#
# Step 1:
# XOR the number with itself right-shifted by 1:
#
#     a = n ^ (n >> 1)
#
# If bits were alternating:
#    n      = 101010
#    n >> 1 = 010101
# XOR        = 111111
#
# So result becomes a number of all 1s.
#
# Step 2:
# Check if 'a' is of the form 111...111
#
# A number with all 1s satisfies:
#
#     a & (a + 1) == 0
#
# Why?
# Example:
#    a = 1111 (binary)
#    a+1 = 10000
#    AND = 0000
#
# That property ONLY works for numbers that are
# consecutive 1s in binary.
#
# ---------------------------------------------
# Time Complexity:
# O(1)
#
# Space Complexity:
# O(1)
#
# This is an optimal bit manipulation trick solution.
