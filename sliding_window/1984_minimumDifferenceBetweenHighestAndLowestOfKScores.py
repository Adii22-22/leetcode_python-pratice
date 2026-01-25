# LeetCode 1984
# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
#
# Approach:
# Sort the array so that any group of k elements will have its minimum at the
# first index of the group and maximum at the last index of the group.
#
# Use a fixed-size sliding window of length k over the sorted array.
# For each window starting at index i, compute the difference:
#   nums[i + k - 1] - nums[i]
# Track the minimum such difference across all valid windows.
#
# If k == 1, the difference is always 0 because a single element has no spread.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space
