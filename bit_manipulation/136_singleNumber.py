# 136. Single Number
# Difficulty: Easy
# Solved on: Nov 21, 2025
#
# Approach:
# - Uses XOR to cancel out duplicate numbers.
# - Property: A ^ A = 0, A ^ 0 = A
# - XORing all numbers leaves only the unique (non-duplicate) element.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int: # type: ignore
        x  = 0
        for num  in nums:
            x = x ^ num
        return x