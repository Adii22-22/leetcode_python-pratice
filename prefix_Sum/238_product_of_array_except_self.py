# LeetCode 238 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
#
# Approach:
# Use prefix and suffix products without using division.
# First pass stores the product of all elements to the left of each index.
# Second pass traverses from right to left and multiplies the product of elements to the right.
# This combines left and right products directly into the output array.
#
# Time Complexity: O(n)
# Space Complexity: O(1) extra space (output array excluded)
