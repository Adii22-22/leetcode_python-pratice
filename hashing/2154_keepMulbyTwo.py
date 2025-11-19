# LeetCode 2154 — Keep Multiplying Found Values by Two
# Difficulty: Easy
# Solved on: Nov 19, 2025
#
# Approach:
# - Convert nums into a set for O(1) membership checks.
# - While 'original' exists in the set, keep multiplying it by 2.
# - The first value of 'original' that is NOT in nums is the answer.
#
# Time Complexity: O(n)
# Space Complexity: O(n)