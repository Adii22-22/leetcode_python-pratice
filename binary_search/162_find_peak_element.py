# LeetCode 162: Find Peak Element
# https://leetcode.com/problems/find-peak-element/
#
# Approach:
# Use binary search based on the slope of the array instead of directly
# checking neighbors. At any index `mid`, compare nums[mid] with nums[mid + 1].
#
# If nums[mid] < nums[mid + 1], the array is rising, so a peak must exist
# on the right side. Move left boundary to mid + 1.
#
# Otherwise, the array is falling (or flat), so a peak exists on the left
# side or at mid. Move right boundary to mid.
#
# Continue until left == right. That index is guaranteed to be a peak.
#
# This avoids boundary checks for mid-1 and mid+1 and works even when the
# peak is at the edges.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
