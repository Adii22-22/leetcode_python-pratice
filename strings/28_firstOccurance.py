# -------------------------------------------------------------
# LeetCode Problem: 28. Find the Index of the First Occurrence in a String
# Solved on: Nov 12, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given two strings haystack and needle, return the index of the
# first occurrence of needle in haystack. If needle is not found,
# return -1.
#
# Example:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
#
# Approach:
# Use a sliding window over the haystack string. Compare each
# substring of length equal to needle with the needle itself.
# If a match is found, return the starting index. If no match is
# present after scanning the full window range, return -1.
# -------------------------------------------------------------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
