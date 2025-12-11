# -------------------------------------------------------------
# LeetCode Problem: 560. Subarray Sum Equals K
# Solved on: Dec 11, 2025
# Difficulty: Medium
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given an integer array nums and an integer k, return the number of
# continuous subarrays whose sum equals k.
#
# Example:
# nums = [1,1,1], k = 2 -> 2
#
# Approach:
# Use prefix sums to maintain the cumulative sum while iterating.
# Maintain a hashmap (prefix_sum -> frequency). For current_sum, the
# number of subarrays ending at this index with sum k equals the frequency
# of (current_sum - k) seen so far. After counting, increment frequency
# of current_sum.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
