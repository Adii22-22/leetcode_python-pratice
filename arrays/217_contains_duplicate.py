"""
LeetCode Problem: 217. Contains Duplicate
Difficulty: Easy
Solved on: Nov 6, 2025

Approach:
---------
Use a set to track numbers seen so far.
As you iterate through the list:
- If a number already exists in the set → a duplicate is found → return True.
- Otherwise, add it to the set and continue.

Time Complexity:  O(n)
Space Complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
