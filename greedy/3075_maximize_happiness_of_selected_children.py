# LeetCode 3075 - Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/
#
# Approach:
# Sort the happiness values in descending order.
# Select up to k children greedily, subtracting the index penalty
# from each selected child's happiness.
# Add only positive effective happiness values to the total.
# Stop early if the effective happiness becomes zero or negative.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int: # type: ignore
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            effective_happiness = happiness[i] - i
            if effective_happiness > 0:
                total += effective_happiness
            else:
                break
        return total