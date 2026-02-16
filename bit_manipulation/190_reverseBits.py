# LeetCode 190
# Problem: Reverse Bits
# Link: https://leetcode.com/problems/reverse-bits/
#
# Approach (Bit Manipulation Simulation):
#
# We reverse the 32-bit representation of the integer.
#
# Steps:
# 1. Initialize result = 0.
# 2. Repeat 32 times (since input is a 32-bit unsigned integer):
#    - Left shift result by 1 to make space for the next bit.
#    - Extract the least significant bit of n using (n & 1).
#    - Add that bit to result using OR.
#    - Right shift n by 1 to process the next bit.
#
# Key Insight:
# We are rebuilding the number bit by bit in reverse order.
# Each iteration:
#   - Take last bit of n
#   - Append it to the left side of result
#
# Why 32 iterations?
# Because the problem guarantees a 32-bit unsigned integer.
#
# Time Complexity: O(1)
#   (Always 32 iterations)
#
# Space Complexity: O(1)
#
# Alternative Pythonic approach:
# Convert to 32-bit binary string, reverse it, and convert back:
#   int('{:032b}'.format(n)[::-1], 2)
#
# However, interviewers usually prefer the bit-manipulation solution.
