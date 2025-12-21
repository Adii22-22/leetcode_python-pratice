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
