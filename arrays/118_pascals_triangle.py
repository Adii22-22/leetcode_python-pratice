# LeetCode 118: Pascal's Triangle
# Date solved: Nov 29, 2025
# Approach: Array Simulation
# Explanation:
#   Begin with the first row [1]. For each new row, start with 1, then fill
#   middle elements by adding adjacent values from the previous row, and end
#   the row with 1. Repeat this process for numRows rows.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]: # type: ignore
        triangle = []

        for _ in range(numRows):
            # start each row with 1
            row = [1]

            # if not the first row, fill middle elements
            if triangle:
                prev = triangle[-1]
                for i in range(1, len(prev)):
                    row.append(prev[i - 1] + prev[i])

                # end each row with 1
                row.append(1)

            triangle.append(row)

        return triangle
