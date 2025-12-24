# LeetCode 3074 - Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/
#
# Approach:
# First compute the total number of apples.
# Sort the box capacities in descending order so that larger boxes are used first.
# Keep adding box capacities until the accumulated capacity is greater than or
# equal to the total apples. The number of boxes used at that point is the answer.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
