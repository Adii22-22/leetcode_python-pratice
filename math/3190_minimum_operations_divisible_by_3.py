# 3190. Minimum Operations to Make All Array Elements Divisible by 3
# Solved on: Nov 22, 2025
#
# Approach:
# For each number, we only care about its remainder when divided by 3.
# - If remainder is 0 → already divisible → no operations required.
# - If remainder is 1 → we can subtract 1 (or add 2), best is subtracting 1 → cost = 1
# - If remainder is 2 → we can subtract 2 or add 1, best is adding 1 → cost = 1
#
# So for any number, the minimum operations = min(rem, 3 - rem)
# Sum these for all numbers.
class Solution:
    def minimumOperations(self, nums: List[int]) -> int: # type: ignore
        operation = 0
        for num in nums:
            remainder = num % 3
            operation += min(remainder, 3 - remainder)
        return operation