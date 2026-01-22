# LeetCode 3507
# Problem: Minimum Pair Removal to Make Array Non-Decreasing
# Link: https://leetcode.com/problems/minimum-pair-removal-to-make-array-non-decreasing/
#
# Approach:
# Repeatedly check if the array is non-decreasing.
# If not, find the adjacent pair with the minimum sum and merge it.
# Each merge reduces the array size by one and counts as one operation.
# Continue until the array becomes non-decreasing.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int: # type: ignore
        operations = 0

        def is_strictly_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True


        while not is_strictly_increasing(nums):
            min_sum = float("inf")
            min_index = 0

            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_index = i

 
            nums[min_index] = min_sum
            nums.pop(min_index + 1)

            operations += 1

        return operations

