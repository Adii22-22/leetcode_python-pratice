# LeetCode 389 - Find the Difference
# https://leetcode.com/problems/find-the-difference/
#
# Approach:
# Use a hash map (dictionary) to count character frequencies.
# First, count all characters in string t.
# Then subtract counts using characters from string s.
# The character with remaining count equal to 1 is the extra character.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
