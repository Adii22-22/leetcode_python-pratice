# ---------------------------------------------------------------
# LeetCode 283: Move Zeroes
# Difficulty: Easy
# Solved on: Nov 11, 2025
#
# Approach:
# Use the Two-Pointer technique.
# - 'read' scans the entire array.
# - 'write' tracks the position where the next non-zero should go.
# Steps:
# 1. Copy all non-zero elements to the front (preserving order).
# 2. After all non-zeros are placed, fill the rest of the array with zeros.
#
# Time Complexity: O(n) – one full pass + one fill pass
# Space Complexity: O(1) – in-place modification
# ---------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None: # type: ignore
        write = 0

        # Move all non-zero elements to front
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Fill the remaining positions with zeros
        for i in range(write, len(nums)):
            nums[i] = 0
