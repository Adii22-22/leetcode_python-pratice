# LeetCode 712: Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
#
# Approach:
# Use Dynamic Programming with memoization.
# Define dp(i, j) as the minimum ASCII delete sum required to make
# the substrings s1[i:] and s2[j:] equal.
#
# Base Cases:
# - If i reaches the end of s1, delete all remaining characters of s2[j:].
# - If j reaches the end of s2, delete all remaining characters of s1[i:].
#
# Transition:
# - If s1[i] == s2[j], no deletion is needed for these characters,
#   so move to dp(i+1, j+1).
# - Otherwise, choose the minimum cost between:
#   1) Deleting s1[i] and moving to dp(i+1, j)
#   2) Deleting s2[j] and moving to dp(i, j+1)
#
# Memoization is used to store results for (i, j) to avoid recomputation.
#
# Time Complexity: O(n * m), where n = len(s1), m = len(s2)
# Space Complexity: O(n * m) due to memoization
