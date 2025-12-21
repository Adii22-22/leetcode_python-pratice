# LeetCode 832 - Flipping an Image
# https://leetcode.com/problems/flipping-an-image/
#
# Approach:
# Iterate through each row of the binary matrix.
# First reverse the row in place.
# Then iterate through the row and invert each bit:
# change 0 to 1 and 1 to 0.
# Modify the matrix in place and return it.
#
# Time Complexity: O(n * m)
# Space Complexity: O(1)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]: # type: ignore
        for rows in image:
            rows.reverse()
            for i in range(len(rows)):
                if rows[i] == 0:
                    rows[i] = 1
                else:
                    rows[i] = 0
        return image