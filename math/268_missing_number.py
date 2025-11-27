# --------------------------------------------------------------
# LeetCode 268 – Missing Number
# Date Solved: Nov 27, 2025
# Pattern: Math / Summation Formula
#
# Problem Summary:
#   You are given an array containing n distinct numbers from
#   the range [0, n]. One number is missing — find it.
#
# Key Idea:
#   Use the Gauss summation formula:
#       expected_sum = n * (n + 1) // 2
#       missing = expected_sum - sum(nums)
#
#   This avoids sorting and achieves the optimal O(n) time.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------------------
