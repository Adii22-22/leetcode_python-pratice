# LeetCode 1009
# Problem: Complement of Base 10 Integer
# Link: https://leetcode.com/problems/complement-of-base-10-integer/
#
# Problem Summary:
# Given a non-negative integer n, return the bitwise complement
# of its binary representation.
#
# The complement flips all bits of the number.
#
# Example:
# n = 5
# binary = 101
# complement = 010 -> 2
#
# ---------------------------------------------------------
# Approach (Bit Mask + XOR):
#
# Step 1: Handle edge case
# If n == 0 → binary is "0"
# Complement should be "1"
#
# Step 2: Create a mask containing all 1s
#
# We compute:
#     mask = (1 << n.bit_length()) - 1
#
# Explanation:
# n.bit_length() gives number of bits needed to represent n.
#
# Example:
# n = 5 (101)
# bit_length = 3
#
# 1 << 3 = 1000
# mask = 1000 - 1 = 111
#
# Step 3: XOR the number with mask
#
# n      = 101
# mask   = 111
# XOR    = 010
#
# This flips every bit.
#
# ---------------------------------------------------------
# Key Insight:
# The mask ensures we only flip the bits that actually
# exist in the number's binary representation.
#
# ---------------------------------------------------------
# Time Complexity:
# O(1)
#
# Space Complexity:
# O(1)
#
# ---------------------------------------------------------
# This is the optimal bit manipulation solution.