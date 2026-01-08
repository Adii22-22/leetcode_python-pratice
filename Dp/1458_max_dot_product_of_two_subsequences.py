# LeetCode 1458: Max Dot Product of Two Subsequences
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/
#
# Approach:
# This problem requires choosing non-empty subsequences from both arrays
# such that their dot product is maximized. Since elements can be negative,
# greedy or sliding window approaches do not work.
#
# Use Dynamic Programming where dp(i, j) represents the maximum dot product
# that can be obtained using nums1[i:] and nums2[j:].
#
# At each state, there are three choices:
# 1) Take both nums1[i] and nums2[j] and add their product.
#    While extending, use max(0, dp(i+1, j+1)) so that a new subsequence
#    can start if extending gives a negative value.
# 2) Skip nums1[i].
# 3) Skip nums2[j].
#
# The base case returns negative infinity to ensure that at least one pair
# of elements is chosen (non-empty subsequence constraint).
#
# Memoization is used to avoid recomputation of overlapping subproblems.
#
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
