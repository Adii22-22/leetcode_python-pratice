# LeetCode 1695 - Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/
#
# Approach:
# Use a sliding window with two pointers and a set to maintain unique elements.
# Expand the window by moving the right pointer and adding elements to the set.
# If a duplicate is found, shrink the window from the left until the duplicate is removed.
# Maintain the current sum of the window and update the maximum sum at each step.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
