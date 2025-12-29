# LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#
# Approach:
# Each row of the matrix is sorted in non-increasing order.
# Apply binary search on each row to find the first negative number.
# All elements to the right of that index are negative.
# Accumulate the count for each row to get the final answer.
#
# Time Complexity: O(m * log n)
# Space Complexity: O(1)
