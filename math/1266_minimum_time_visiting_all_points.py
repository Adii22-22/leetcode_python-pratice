# LeetCode 1266: Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/
#
# Approach:
# The time required to move from one point to another depends on the maximum
# of the absolute differences in x and y coordinates.
#
# This is because in one second, we can move:
# - horizontally,
# - vertically, or
# - diagonally.
#
# Diagonal movement reduces both x and y differences at the same time,
# so the minimum time between two points is:
# max(|x1 - x2|, |y1 - y2|)
#
# Iterate through consecutive point pairs, compute the required time
# for each move, and accumulate the total time.
#
# Time Complexity: O(n), where n is the number of points
# Space Complexity: O(1)
