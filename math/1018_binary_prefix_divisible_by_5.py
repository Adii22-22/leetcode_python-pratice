"""
1018. Binary Prefix Divisible By 5
Difficulty: Easy
Date Solved: Nov 24, 2025

Approach:
- We build the binary number prefix-by-prefix.
- Instead of converting the full binary string each time (very slow),
  we maintain the remainder (modulo 5) of the current prefix.
- For each new bit, the new value = old_value * 2 + bit.
- But we keep only remainder modulo 5: rem = (rem * 2 + bit) % 5
- If rem == 0, then the prefix is divisible by 5.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]: # type: ignore
        result = []
        rem = 0
        for bit in nums:
            rem = (rem * 2 + bit) % 5
            result.append(rem == 0)
        return result