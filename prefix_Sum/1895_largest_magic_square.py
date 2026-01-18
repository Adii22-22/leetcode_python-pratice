# LeetCode 1895: Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/
#
# Approach:
# A k x k magic square requires:
# - All row sums to be equal
# - All column sums to be equal
# - Both diagonal sums to be equal
#
# To efficiently check sums of rows, columns, and diagonals for any sub-square,
# we precompute prefix sum matrices:
# 1. row prefix sums for fast row sum queries
# 2. column prefix sums for fast column sum queries
# 3. main diagonal (top-left to bottom-right) prefix sums
# 4. anti-diagonal (top-right to bottom-left) prefix sums
#
# Using these prefix sums, each sum query is reduced to O(1).
# We then try all possible square sizes k from 2 up to min(m, n),
# and for each position (i, j), verify whether the k x k square
# satisfies the magic square conditions.
#
# The answer is the maximum k for which a valid magic square exists.
# A 1x1 square is always magic, so the answer starts at 1.
#
# Time Complexity: O(m * n * min(m, n))
# Space Complexity: O(m * n)
