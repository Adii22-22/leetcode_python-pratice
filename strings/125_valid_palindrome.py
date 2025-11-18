# -------------------------------------------------------------
# LeetCode Problem: 125. Valid Palindrome
# Solved on: Nov 3, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Example:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
#
# Approach:
# 1. Build a cleaned string containing only lowercase alphanumeric characters.
# 2. Compare the cleaned string with its reverse to check if it forms a palindrome.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char.lower()
        return cleaned_s == cleaned_s[::-1]
