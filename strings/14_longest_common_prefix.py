# -------------------------------------------------------------
# LeetCode Problem: 14. Longest Common Prefix
# Solved on: Nov 5, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Explanation:
# Compare characters of each string one by one from the start.
# Shorten the prefix when a mismatch occurs.
#
# Approach:
# 1. Take the first word as the initial prefix.
# 2. Iterate through all other words:
#    - While the current word does not start with the prefix,
#      shorten the prefix by one character from the end.
# 3. If the prefix becomes empty, return "".
# 4. After all iterations, return the final prefix.
#
# Time Complexity: O(n * m)
#   where n = number of strings, m = average string length.
# Space Complexity: O(1)
# -------------------------------------------------------------

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pre = strs[0]
        for word in strs[1:]:
            while not word.startswith(pre):
                pre = pre[:-1]
                if not pre:
                    return ""
        return pre
