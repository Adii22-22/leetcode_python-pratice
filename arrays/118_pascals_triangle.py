# LeetCode 118: Pascal's Triangle
# Date solved: Nov 29, 2025
# Approach: Array Simulation
# Explanation:
#   Begin with the first row [1]. For each new row, start with 1, then fill
#   middle elements by adding adjacent values from the previous row, and end
#   the row with 1. Repeat this process for numRows rows.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
