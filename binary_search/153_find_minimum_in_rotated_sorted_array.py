# LeetCode 153 - Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Approach:
# Use binary search to find the minimum element in a rotated sorted array.
# Compare the middle element with the rightmost element to decide
# which half contains the minimum.
# If nums[mid] > nums[right], the minimum lies in the right half.
# Otherwise, the minimum lies in the left half (including mid).
# Continue narrowing the search space until left == right.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int: # type: ignore
        left = 0
        right = len(nums) -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]