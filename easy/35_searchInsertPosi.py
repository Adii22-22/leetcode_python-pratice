# -------------------------------------------------------------
# LeetCode Problem: 35. Search Insert Position
# Solved on: Nov 12, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be inserted in order.
#
# Example:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Approach:
# Iterate through the array and return the first index where the
# value is greater than or equal to the target. If no such index
# exists, the target belongs at the end of the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
