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
