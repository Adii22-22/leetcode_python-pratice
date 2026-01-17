# LeetCode 3047: Largest Square Area
# https://leetcode.com/problems/largest-square-area/
#
# Approach:
# We are given multiple axis-aligned rectangles, each defined by its
# bottom-left and top-right coordinates.
#
# For every pair of rectangles, we compute their overlapping region:
# - The overlapping width is the minimum of right x-coordinates minus
#   the maximum of left x-coordinates.
# - The overlapping height is the minimum of top y-coordinates minus
#   the maximum of bottom y-coordinates.
#
# If both width and height are positive, the overlapping region exists.
# The largest square that can fit inside this overlap has side length
# equal to min(width, height).
#
# We iterate over all pairs of rectangles, track the maximum possible
# square side length, and finally return its area.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)
