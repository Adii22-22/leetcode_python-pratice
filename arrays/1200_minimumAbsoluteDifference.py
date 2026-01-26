# LeetCode 1200
# Problem: Minimum Absolute Difference
# Link: https://leetcode.com/problems/minimum-absolute-difference/
#
# Approach:
# First sort the array so that the minimum absolute difference must occur
# between adjacent elements.
#
# Iterate through the sorted array and compute the difference between every
# adjacent pair.
#
# If a smaller difference than the current minimum is found, update the
# minimum and reset the result list with the new pair.
#
# If the difference equals the current minimum, append the pair to the result.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space (excluding output list)
