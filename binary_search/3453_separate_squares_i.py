# LeetCode 3453: Separate Squares I
# https://leetcode.com/problems/separate-squares-i/
#
# Approach:
# We are asked to find the minimum y-coordinate of a horizontal line such that
# the total area of all squares above the line equals the total area below it.
#
# Each square is treated independently (overlapping areas are counted multiple times),
# so for a given height H, we can compute how much area of each square lies:
# - completely above the line,
# - completely below the line, or
# - split by the line.
#
# For a candidate height H:
# - If H is below a square, its entire area contributes to "above".
# - If H is above a square, its entire area contributes to "below".
# - If H cuts the square, the square is split proportionally by height.
#
# Define a function that returns (below_area - above_area) for a given H.
# As H increases, below_area increases and above_area decreases monotonically.
# This allows us to apply binary search on the answer.
#
# Binary search is performed between:
# - the minimum y-coordinate of all squares, and
# - the maximum (y + side length) of all squares.
#
# The search continues until the range is within a small precision (1e-6),
# which is sufficient for the required accuracy.
#
# Time Complexity: O(n * log R), where n is number of squares and R is the y-range
# Space Complexity: O(1)
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float: # type: ignore
        low = min(y for _,y,_ in squares)
        high  = max(y+l for _,y,l in squares)
        
        def area_diff(h):
            below = 0
            above = 0
            for square  in squares:
                bottom = square[1]
                top  = square[1]+square[2]
                area = square[2] * square[2]

                if h <= bottom:
                    above+=area
                elif h >=top:
                    below+=area
                else:
                    height_below = h - bottom
                    height_above = top - h

                    below += square[2] * height_below
                    above += square[2] * height_above
            return below - above
        
        while (high-low) > 1e-6:
            mid = (high+low) / 2

            diff = area_diff(mid)

            if diff < 0:
                low = mid
            else:
                high = mid
        return low