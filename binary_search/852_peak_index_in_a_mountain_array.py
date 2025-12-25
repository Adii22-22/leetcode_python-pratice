# LeetCode 852 - Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
#
# Approach:
# Use binary search on the mountain array.
# Compare arr[mid] with arr[mid + 1] to determine slope direction.
# If arr[mid] < arr[mid + 1], the peak lies to the right.
# Otherwise, the peak lies to the left or at mid.
# Narrow the search space until left == right.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int: # type: ignore
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left