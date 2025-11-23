# 1262. Greatest Sum Divisible by Three
# Difficulty: Medium
# Date Solved: Nov 23, 2025
#
# Approach:
# - Compute the total sum of the array.
# - If total % 3 == 0 → we can return total immediately.
# - Otherwise:
#     • Numbers with remainder 1 and remainder 2 (mod 3) are separated.
#     • We track the two smallest numbers in each category:
#         - smallest and second smallest with remainder 1
#         - smallest and second smallest with remainder 2
# - For remainder 1:
#     Option A: remove smallest remainder-1 number
#     Option B: remove two smallest remainder-2 numbers
#
# - For remainder 2:
#     Option A: remove smallest remainder-2 number
#     Option B: remove two smallest remainder-1 numbers
#
# - Return the maximum valid sum.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
