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
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int: # type: ignore
        seconds = 0
        for i in range(len(points)-1):
            current_points = points[i]
            next_points = points[i+1]

            seconds += max(abs(current_points[0]- next_points[0]), abs(current_points[1] - next_points[1]))
        return seconds
        