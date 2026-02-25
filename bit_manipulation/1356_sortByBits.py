# LeetCode 1356
# Problem: Sort Integers by The Number of 1 Bits
# Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
#
# Problem Summary:
# Sort the array based on:
# 1️⃣ Number of set bits (1s) in binary representation.
# 2️⃣ If tie → sort by numeric value.
#
# Example:
# arr = [0,1,2,3,4,5,6,7,8]
# Binary:
# 0 -> 0        (0 bits)
# 1 -> 1        (1 bit)
# 2 -> 10       (1 bit)
# 3 -> 11       (2 bits)
# ...
#
# ---------------------------------------------------------
# Approach (Brian Kernighan’s Algorithm):
#
# We define a helper function count_bits(n):
#
# While n > 0:
#     n = n & (n - 1)
#     count += 1
#
# Key Insight:
# n & (n - 1) removes the lowest set bit in n.
#
# Example:
# n = 12 (1100)
# n-1 = 11 (1011)
# AND  = 1000 (lowest 1 removed)
#
# This runs in O(number_of_set_bits).
#
# Then we sort using:
# key = (count_bits(x), x)
#
# Meaning:
# - Primary sort → number of set bits
# - Secondary sort → numeric value
#
# ---------------------------------------------------------
# Time Complexity:
# Counting bits → O(log n) worst case per number
# Sorting → O(n log n)
# Overall → O(n log n)
#
# Space Complexity:
# O(log n) recursion stack (internally for sorting)
#
# ---------------------------------------------------------
# Pythonic Alternative:
# Python provides built-in bit_count():
#
# sorted(arr, key=lambda x: (x.bit_count(), x))
#
# Cleaner and faster in practice.


#Brian Kernighan's Algorithm
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]: # type: ignore
        def count_bits(n:int) -> int:
            count = 0
            while n > 0:
                n = n & (n-1)
                count+=1
            return count
        return sorted(arr,key=lambda x : (count_bits(x),x))

#pythonic solution 
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         return sorted(arr,key= lambda x: (x.bit_count(),x))