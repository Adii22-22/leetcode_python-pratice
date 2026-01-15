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
from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_consecutive_run(bars: List[int]) -> int:
            if not bars:
                return 1
            
            bars.sort()
            longest = 1
            curr = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            
            return longest + 1 
        
        max_h = longest_consecutive_run(hBars)
        max_v = longest_consecutive_run(vBars)
        
        side = min(max_h, max_v)
        return side * side
