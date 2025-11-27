# --------------------------------------------------------------
# LeetCode 66 – Plus One
# Date Solved: Nov 26, 2025
# Pattern: Math / Array Manipulation
#
# Problem Summary:
#   Given a list of digits representing a non-negative integer,
#   increment the integer by one and return the resulting digits.
#
# Key Idea:
#   Work from the last digit backwards:
#     • If digit < 9 → just add 1 and return.
#     • If digit == 9 → convert it to 0 and continue carry backward.
#   If all digits were 9 (e.g., 999), final answer becomes 1000.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (modifies list in place)
# --------------------------------------------------------------
