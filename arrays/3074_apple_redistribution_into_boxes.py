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
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int: # type: ignore
        total_apple = sum(apple)
        capacity.sort(reverse=True)
        box_sum = 0
        for i in range(0,len(capacity)):
            box_sum += capacity[i]
            if box_sum >= total_apple:
                return i+1