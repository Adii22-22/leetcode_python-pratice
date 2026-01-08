# LeetCode 930: Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/
#
# Approach:
# Use Prefix Sum with a HashMap to count the number of subarrays whose sum
# equals the given goal.
#
# Maintain a running prefix sum while iterating through the array.
# For the current prefix sum `total`, any previous prefix sum equal to
# `total - goal` will form a subarray ending at the current index
# with sum equal to goal.
#
# Store the frequency of each prefix sum in a hashmap.
# Initialize the hashmap with {0: 1} to correctly handle subarrays
# that start from index 0.
#
# This approach works efficiently even with zeros in the array,
# where sliding window techniques fail.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int: # type: ignore
        count = 0
        dictt = defaultdict(int) # type: ignore
        total = 0
        dictt[0] = 1
        for num in nums:
            total += num
            count += dictt[total-goal]
            dictt[total] += 1
        return count