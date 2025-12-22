# LeetCode 520 - Detect Capital
# https://leetcode.com/problems/detect-capital/
#
# Approach:
# Use Python built-in string methods to validate correct capital usage.
# The word is valid if all letters are uppercase, all letters are lowercase,
# or only the first letter is uppercase (title case).
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() or word.isupper() or word.islower()
