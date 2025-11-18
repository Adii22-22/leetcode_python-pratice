# -------------------------------------------------------------
# LeetCode Problem: 27. Remove Element
# Solved on: Nov 11, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The order of elements
# may change. Return the number of elements remaining after
# removal. Elements beyond the returned length do not matter.
#
# Example:
# Input: nums = [3,2,2,3], val = 3
# Output: 2
#
# Approach:
# Use two pointers (read and write). Traverse the array with
# the read pointer and copy every value not equal to val to
# the write pointer position. The write pointer represents
# the position of the next valid element. Finally, return the
# count of valid elements (write).
# -------------------------------------------------------------

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # type: ignore
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write
