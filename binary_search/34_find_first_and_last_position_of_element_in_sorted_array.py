# LeetCode 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Approach:
# Use two separate binary searches on the same sorted array.
# The first binary search finds the leftmost (first) occurrence of the target
# by recording the index when found and continuing to search the left half.
# The second binary search finds the rightmost (last) occurrence by recording
# the index when found and continuing to search the right half.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
