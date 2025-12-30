# LeetCode 11 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
#
# Approach:
# Use two pointers starting from both ends of the array.
# At each step, calculate the area using the minimum of the two heights
# and the distance between the pointers.
# Move the pointer pointing to the smaller height, since the area is
# always limited by the shorter line.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
