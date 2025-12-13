# -------------------------------------------------------------
# LeetCode Problem: 387. First Unique Character in a String
# Solved on: Dec 13, 2025
# Difficulty: Easy
# Language: Python
# Pattern: Hashing / Frequency Count
# -------------------------------------------------------------
# Problem Statement:
# Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1.
#
# Example:
# Input: s = "leetcode"
# Output: 0
#
# Input: s = "loveleetcode"
# Output: 2
#
# Approach:
# 1. Use a hash map to count the frequency of each character.
# 2. Traverse the string again in order.
# 3. Return the first index where character frequency is 1.
#
# Time Complexity: O(n)
# Space Complexity: O(1) — fixed alphabet size
# -------------------------------------------------------------
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_char = defaultdict(int) # type: ignore

        for char in s:
            unique_char[char] +=1
            
        for first in range(len(s)):
            if unique_char[s[first]] == 1:
                return first

        return -1
