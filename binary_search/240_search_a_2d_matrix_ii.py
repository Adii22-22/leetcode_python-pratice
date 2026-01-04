# LeetCode 240: Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/
#
# Approach:
# Start from the top-right corner of the matrix.
# At any position:
# - If the current value is greater than the target, move left to reduce values.
# - If the current value is smaller than the target, move down to increase values.
#
# This works because each row is sorted left to right and each column is sorted
# top to bottom. Each move eliminates an entire row or column from consideration.
#
# Time Complexity: O(m + n)
# Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        row = 0
        col = len(matrix[row])-1

        while row < len(matrix) and col >=0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -=1
            else:
                row +=1
        return False