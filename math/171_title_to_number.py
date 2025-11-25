#LeetCode 171. Excel Sheet Column Number
# Difficulty: Easy
# Date Solved: Nov 25, 2025
#
# Pattern: Math / Base Conversion
#
# Approach:
# Excel column titles represent a base-26 number system:
#   A = 1, B = 2, ..., Z = 26
#
# For example:
#   "A"   -> 1
#   "Z"   -> 26
#   "AA"  -> 27  (1*26 + 1)
#
# We iterate left-to-right, and for each character:
#   letter_value = ord(char) - ord('A') + 1
#   num = num * 26 + letter_value
#
# Time Complexity: O(n)
# Space Complexity: O(1)
