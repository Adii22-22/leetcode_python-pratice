# LeetCode 1877
# Problem: Minimize Maximum Pair Sum in Array
# Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
#
# Approach:
# First sort the array so numbers are in ascending order.
# Use two pointers: one starting from the beginning (smallest element)
# and one from the end (largest element).
#
# Pair the smallest and largest elements together, because pairing extremes
# balances the sums and prevents large numbers from forming a very large pair.
#
# For each such pair, compute the pair sum and track the maximum among them.
# The answer is the maximum pair sum obtained using this pairing strategy.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space
