# -------------------------------------------------------------
# LeetCode Problem: 58. Length of Last Word
# Solved on: Nov 8, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a string s consisting of words and spaces, return the length
# of the last word in the string.
# A word is defined as a maximal substring consisting of non-space
# characters only.
#
# Example:
# Input: s = "Hello World"
# Output: 5
#
# Approach:
# Iterate backward through the string to efficiently skip trailing
# spaces and count the characters of the last word.
# - Initialize length = 0
# - Traverse from the end:
#   • Skip trailing spaces
#   • Count non-space characters until another space is found
# - Return the count as the length of the last word.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == " " and length > 0:
                break
            elif s[i] != " ":
                length += 1
        return length
