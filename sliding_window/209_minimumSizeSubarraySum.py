# -------------------------------------------------------------------------------
# LeetCode 209: Minimum Size Subarray Sum
# Difficulty: Medium
# Date Solved: Nov 17, 2025
#
# Problem:
# Given an array of positive integers `nums` and a target value, find the minimal
# length of a contiguous subarray whose sum is >= target. If no such subarray 
# exists, return 0.
#
# Approach: Sliding Window (Two Pointers)
#
# - Since all numbers are positive, increasing the window always increases the sum.
# - Use two pointers: `left_pointer` (start of window) and `right_pointer` (end).
# - Expand the window by moving `right_pointer` forward and adding to `current_sum`.
# - When the window sum becomes >= target, shrink the window from the left to find
#   the smallest possible valid window.
# - Track the minimum window length found.
#
# Why This Works:
# - Each index is visited at most twice (once by right pointer, once by left).
# - This gives an optimal O(n) solution.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------------------------
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: # type: ignore
        left_pointer = 0
        current_sum  = 0
        right_pointer = 0
        min_length = float('inf')
        
        for right_pointer in range(len(nums)):
            current_sum += nums[right_pointer]
        
            while current_sum >= target:
                window_length = right_pointer - left_pointer + 1
                min_length = min(min_length,window_length)
                current_sum -= nums[left_pointer]
                left_pointer +=1
        if min_length == float('inf'):
            return 0
        else:
            return min_length











        