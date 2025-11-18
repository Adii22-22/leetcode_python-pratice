# --------------------------------------------------------------------------------
# LeetCode 643: Maximum Average Subarray I
# Difficulty: Easy
# Date Solved: Nov 12, 2025
#
# Problem:
# Given an integer array `nums` and an integer `k`, find the contiguous subarray 
# of length `k` that has the maximum average value, and return that average.
#
# Approach: Sliding Window
#
# - First compute the sum of the initial window of size `k`.
# - Then slide the window across the array:
#     - Add the element entering the window.
#     - Subtract the element leaving the window.
# - Track the maximum window sum encountered.
# - Divide the maximum sum by `k` to get the maximum average.
#
# Why It Works:
# - Sliding window allows updating the sum in O(1) time per step.
# - Total complexity is linear since each element is processed once.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------------------------------------------------------
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: # type: ignore
        window_sum = sum(nums[0:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum/k

        