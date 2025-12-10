# -------------------------------------------------------------
# LeetCode Problem: 33. Search in Rotated Sorted Array
# Solved on: Dec 10, 2025
# Difficulty: Medium
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a rotated sorted array nums and a target value, return the
# index of the target if it exists. If not, return -1. The array was
# originally sorted in ascending order and then rotated.
#
# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Approach:
# Use modified binary search.
# - Determine which half (left or right) is sorted.
# - If target lies inside the sorted half, search there.
# - Otherwise, search the other half.
# This maintains O(log n) performance.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left)// 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid+1
            else:
                if nums[mid] <target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
            
