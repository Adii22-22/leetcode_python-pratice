# -------------------------------------------------------------
# LeetCode Problem: 13. Roman to Integer
# Solved on: Nov 3, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Convert a Roman numeral into an integer.
#
# Roman numerals are represented by seven different symbols:
# I, V, X, L, C, D, and M.
#
# Example:
# Input: s = "MCMXCIV"
# Output: 1994
#
# Explanation:
# - Start from the end of the string.
# - If a symbol's value is less than the previous one, subtract it.
# - Otherwise, add it.
# - Continue until the start of the string.
#
# Approach:
# 1. Create a mapping (dictionary) for all Roman symbols and their integer values.
# 2. Traverse the string in reverse.
# 3. Compare each symbol's value with the previous one:
#    - If smaller → subtract it.
#    - Else → add it.
# 4. Return the total.
# -------------------------------------------------------------

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        pre_value = 0

        for char in reversed(s):
            value = roman_dict[char]
            if value < pre_value:
                total -= value
            else:
                total += value
            pre_value = value
        return total
