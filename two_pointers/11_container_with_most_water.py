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
class Solution:
    def maxArea(self, height: List[int]) -> int: # type: ignore
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        while left < right:
            h = min(height[left],height[right])
            width = right -left
            area = h * width 
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area