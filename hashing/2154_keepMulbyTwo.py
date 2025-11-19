# LeetCode 2154 — Keep Multiplying Found Values by Two
# Difficulty: Easy
# Solved on: Nov 19, 2025
#
# Approach:
# - Convert nums into a set for O(1) membership checks.
# - While 'original' exists in the set, keep multiplying it by 2.
# - The first value of 'original' that is NOT in nums is the answer.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int: # type: ignore
        new_nums = set(nums)

        # Keep doubling while original is found in the set
        while original in new_nums:
            original *= 2

        return original