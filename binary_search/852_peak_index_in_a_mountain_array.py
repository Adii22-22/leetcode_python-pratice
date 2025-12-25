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
