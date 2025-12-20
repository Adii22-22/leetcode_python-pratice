# LeetCode 724 - Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
#
# Approach:
# First compute the total sum of the array.
# Maintain a running left sum while iterating through the array.
# At each index, calculate the right sum as:
# total_sum - left_sum - current_element.
# If left sum equals right sum, return the current index.
# Update left sum after checking the pivot condition.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int: # type: ignore
        total = sum(nums)
        left_sum = 0
        for i in range(0,len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1