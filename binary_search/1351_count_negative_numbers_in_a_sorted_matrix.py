# LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#
# Approach:
# Each row of the matrix is sorted in non-increasing order.
# Apply binary search on each row to find the first negative number.
# All elements to the right of that index are negative.
# Accumulate the count for each row to get the final answer.
#
# Time Complexity: O(m * log n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_count = 0
        for row in range(0,len(grid)):
            l = 0
            r = len(grid[row]) -1
            while l<=r:
                mid = l + (r-l)//2
                if grid[row][mid] < 0:
                    r = mid-1
                else:
                    l = mid+1
            negative_count += len(grid[row]) - l
        return negative_count