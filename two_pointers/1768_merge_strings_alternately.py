# LeetCode 1768 - Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/
#
# Approach:
# Use two pointers to traverse both strings simultaneously.
# Append characters alternately from each string while both pointers are valid.
# Once one string is exhausted, append the remaining substring of the other string.
# Join the collected characters to form the final merged string.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
