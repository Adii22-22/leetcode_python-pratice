# -------------------------------------------------------------
# LeetCode Problem: 9. Palindrome Number
# Solved on: Nov 2, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
#
# Example:
# Input: x = 121
# Output: True
#
# Approach:
# Convert the integer to a string and compare it with its reverse.
# If both are equal, it's a palindrome.
# -------------------------------------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool: 
        s = str(x)
        return s[::-1] == s
