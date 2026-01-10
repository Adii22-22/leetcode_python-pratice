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
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == len(s1) or j == len(s2):
                if i == len(s1):
                    return sum(ord(ch) for ch in s2[j:])
                else:
                    return sum(ord(ch) for ch in s1[i:])
            
            if s1[i] == s2[j]:
                result = dp(i+1,j+1)
                memo[(i,j)] = result
                return result
            else:
                result = min(ord(s1[i]) + dp(i+1,j), ord(s2[j]) + dp(i,j+1))
                memo[(i,j)] = result
                return result

        return dp(0,0)