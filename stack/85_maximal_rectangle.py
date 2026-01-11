# LeetCode 85: Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
#
# Approach:
# Treat each row of the matrix as the base of a histogram.
# Maintain an array `heights` where heights[i] represents the number of
# consecutive '1's in column i up to the current row.
#
# For each row:
# 1) Update the histogram heights:
#    - If matrix[row][i] == '1', increment heights[i]
#    - Otherwise, reset heights[i] to 0
#
# 2) Apply the "Largest Rectangle in Histogram" algorithm using a stack:
#    - Traverse through the heights array
#    - Maintain a monotonic increasing stack of indices
#    - When a smaller height is encountered, pop from the stack and
#      calculate area using the popped height as the smallest bar
#    - Append a virtual 0 height at the end to flush the stack
#
# Track the maximum rectangle area across all rows.
#
# Time Complexity: O(rows * cols)
# Space Complexity: O(cols)
