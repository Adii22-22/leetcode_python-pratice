# LeetCode 961: N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
#
# Approach:
# Use a set to track seen elements. Since exactly one element appears N times
# and all others appear once, the first duplicate encountered during traversal
# must be the repeated element. Return immediately on detection.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int: # type: ignore
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)