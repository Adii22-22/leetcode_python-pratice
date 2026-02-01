# LeetCode 3010
# Problem: Divide an Array Into Subarrays With Minimum Cost I
# Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
#
# Approach:
# The array must be divided into exactly 3 contiguous subarrays.
# The cost of each subarray is its first element.
#
# The first subarray must start at index 0, so nums[0] is always included.
# To minimize total cost, we only need to choose the starting indices
# of the 2nd and 3rd subarrays from the remaining elements.
#
# Therefore, we pick the two smallest values from nums[1:].
# Total cost = nums[0] + smallest + second smallest.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space (ignoring input array)
class Solution:
    def minimumCost(self, nums: List[int]) -> int: # type: ignore
        rest = nums[1:]
        rest.sort()
        return nums[0] + rest[0] + rest[1]
