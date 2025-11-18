# LeetCode Problem: 1. Two Sum
# Difficulty: Easy
# Date Solved: Sept 2, 2025
# Link: https://leetcode.com/problems/two-sum/
# Approach: Hash Map (O(n) time)
# Note: Solved with help to understand the logic

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Use a hash map to store seen numbers and their indices.
        For each number, check if its complement (target - num) has been seen.
        If yes, return the indices.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
