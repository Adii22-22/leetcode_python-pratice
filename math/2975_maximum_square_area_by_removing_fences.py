# LeetCode 2975: Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
#
# Approach:
# We are given horizontal and vertical fences in a rectangular field.
# By removing fences, we can form larger continuous segments.
#
# First, include the boundary fences (1 and m / n) along with the given fences
# and sort them. Then, compute all possible distances between pairs of horizontal
# fences and store them in a set.
#
# Next, compute all possible distances between pairs of vertical fences.
# If a vertical distance exists in the horizontal distance set, it can form
# a square. Track the maximum such distance.
#
# If no valid square can be formed, return -1.
# Otherwise, return the area of the largest square modulo 1e9 + 7.
#
# Time Complexity: O(h^2 + v^2)
# Space Complexity: O(h^2)
