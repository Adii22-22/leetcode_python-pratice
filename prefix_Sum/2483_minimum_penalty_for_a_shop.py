# LeetCode 2483 - Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/
#
# Approach:
# Treat the problem as tracking how the penalty changes as the closing time moves.
# Initially assume the shop closes at hour 0, so all 'Y' contribute to the penalty.
# As the closing time moves forward:
# - Passing a 'Y' decreases the penalty (customer is served).
# - Passing an 'N' increases the penalty (shop was open without customers).
# Track the minimum penalty seen and the corresponding closing time.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
