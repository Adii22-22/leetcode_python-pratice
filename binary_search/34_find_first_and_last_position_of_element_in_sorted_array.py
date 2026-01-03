# LeetCode 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Approach:
# Use two separate binary searches on the same sorted array.
# The first binary search finds the leftmost (first) occurrence of the target
# by recording the index when found and continuing to search the left half.
# The second binary search finds the rightmost (last) occurrence by recording
# the index when found and continuing to search the right half.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # type: ignore
        low = 0
        high = len(nums)-1
        left_answer = -1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                left_answer = mid
                high = mid-1   
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
            
        low = 0
        high = len(nums)-1 
        right_answer = -1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                right_answer = mid
                low  = mid+1  
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        return left_answer,right_answer