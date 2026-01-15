# LeetCode 2943: Maximize Square Hole Area
# https://leetcode.com/problems/maximize-square-hole-area/
#
# Approach:
# When bars are removed consecutively, adjacent cells merge.
# A consecutive run of k removed bars creates (k + 1) merged cells.
#
# To form a square hole, we need merged cells in BOTH directions:
# - horizontal (from hBars)
# - vertical (from vBars)
#
# Steps:
# 1. Sort the removed horizontal bars and find the longest run where
#    bars[i] == bars[i - 1] + 1.
# 2. Do the same for vertical bars.
# 3. Each longest run of length k creates (k + 1) cells.
# 4. The maximum square side is the minimum of horizontal and vertical cells.
# 5. Return side * side as the area.
#
# Time Complexity: O(h log h + v log v)
# Space Complexity: O(1)
