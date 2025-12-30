# LeetCode 15 - 3Sum
# https://leetcode.com/problems/3sum/
#
# Approach:
# Sort the array and fix one element using an index i.
# For each fixed element, use two pointers (left and right) to find pairs
# such that the sum of the three numbers equals zero.
# Move pointers based on whether the current sum is too small or too large.
# Skip duplicate values for the fixed index and for both pointers to ensure
# that only unique triplets are added to the result.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra space (output list excluded)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: # type: ignore
        threeSum = []
        n = len(nums)
        nums.sort()
        for i in range(0,n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            fixed = nums[i]
            left = i+1
            right = n-1
            while left < right:
                current_sum = nums[i] + nums[right] + nums[left]
                if current_sum < 0:
                    left+=1
                elif current_sum > 0:
                    right-=1
                else:
                    threeSum.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return threeSum