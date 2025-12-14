# -------------------------------------------------------------
# LeetCode Problem: 438. Find All Anagrams in a String
# Difficulty: Medium
# Pattern: Sliding Window + Hash Map
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given two strings s and p, return all start indices of p's
# anagrams in s.
#
# Approach:
# Use a sliding window of size len(p).
# Maintain two hash maps:
# - need: frequency of characters in p
# - window: frequency of current window in s
# Slide the window and compare maps.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
