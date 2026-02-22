# LeetCode 868
# Problem: Binary Gap
# Link: https://leetcode.com/problems/binary-gap/
#
# Problem Summary:
# Given an integer n, return the maximum distance between
# two consecutive 1's in its binary representation.
#
# Example:
# n = 22
# binary = 10110
# Positions of 1s → 0, 2, 3
# Distances → 2 and 1
# Answer → 2
#
# ---------------------------------------------------------
# Approach (Pure Bit Manipulation):
#
# Instead of converting to a binary string, we process bits directly.
#
# 1. Maintain:
#    - position → current bit index (starting from 0)
#    - last_one_seen → index of previous '1'
#    - max_distance → maximum gap found
#
# 2. While n > 0:
#    - Check if last bit is 1 using (n & 1)
#    - If yes:
#         • compute distance from last_one_seen
#         • update max_distance
#         • update last_one_seen
#
# 3. Right shift n (n >>= 1) to process next bit.
# 4. Increment position.
#
# ---------------------------------------------------------
# Why (n & 1)?
# It extracts the least significant bit.
#
# Why shift right?
# To move to the next bit.
#
# ---------------------------------------------------------
# Time Complexity:
# O(log n)
# (number of bits in n)
#
# Space Complexity:
# O(1)
#
# ---------------------------------------------------------
# This is more optimal than the string-based version
# because it avoids creating a binary string.
class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        last_one_seen = -1
        position = 0
        
        while n > 0:
            if n & 1 == 1: 
                if last_one_seen != -1:
                    max_distance = max(max_distance, position - last_one_seen)
                last_one_seen = position
            
            n >>= 1 
            position += 1
            
        return max_distance
#less optimal
class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        last_one_seen = -1
        s = bin(n)
        for i, digit in enumerate(s):
            if digit == '1':
                if last_one_seen != -1:
                    max_distance = max(max_distance,(i-last_one_seen))
                last_one_seen = i
        return max_distance