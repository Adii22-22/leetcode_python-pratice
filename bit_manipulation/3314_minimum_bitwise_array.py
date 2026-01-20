# LeetCode 3314: Minimum Bitwise Array
# https://leetcode.com/problems/minimum-bitwise-array/
#
# Approach:
# For each number in the array, we want to find the minimum possible value
# such that performing a bitwise AND operation pattern (as defined by the problem)
# produces the given number.
#
# Observation:
# The smallest valid value can be obtained by turning off the lowest set bit
# in the number. To do this, we iterate over powers of two (bit masks) starting
# from the least significant bit.
#
# As long as the current bit is set, subtracting that power of two yields a
# smaller candidate value. The first time we encounter an unset bit, we stop.
#
# If no such subtraction is possible, the result remains -1.
#
# This process is repeated independently for each element in the array.
#
# Time Complexity: O(n * log M), where M is the maximum value in nums
# Space Complexity: O(1)
