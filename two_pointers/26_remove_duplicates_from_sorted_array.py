# -------------------------------------------------------------
# LeetCode Problem: 26. Remove Duplicates from Sorted Array
# Solved on: Nov 4, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a sorted array nums, remove the duplicates in-place such that
# each element appears only once and return the new length.
# Do not allocate extra space for another array; modify the input array
# in-place with O(1) extra memory.
#
# Example:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#
# Approach:
# Use two pointers:
# - 'write_pointer' keeps track of the last unique element position.
# - 'read_pointer' scans the array.
# When a new unique element is found, increment the write_pointer and
# copy that element to the new position.
# Return the count of unique elements as write_pointer + 1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------

class Solution:
    def removeDuplicates(nums) -> int:
        write_pointer = 0
        read_pointer = 1
        if not nums:
            return 0
        for read_pointer in range(1, len(nums)):
            if nums[read_pointer] != nums[write_pointer]:
                write_pointer += 1
                nums[write_pointer] = nums[read_pointer]
        return write_pointer + 1
