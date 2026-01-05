# LeetCode 1975: Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/
#
# Approach:
# Traverse the entire matrix once and focus on absolute values instead of signs.
# Flipping elements does not change their absolute value, so the goal is to
# maximize the total sum of absolute values.
#
# While scanning the matrix:
# - Keep track of the sum of absolute values
# - Count how many negative numbers exist in the entire matrix
# - Track the smallest absolute value
#
# If the total number of negative elements is even, all values can be made positive
# and the answer is simply the sum of absolute values.
# If the count is odd, one element must remain negative; to minimize loss, subtract
# twice the smallest absolute value from the total.
#
# Time Complexity: O(m * n)
# Space Complexity: O(1)
