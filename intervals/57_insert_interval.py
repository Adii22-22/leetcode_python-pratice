# LeetCode 57
# Problem: Insert Interval
# Link: https://leetcode.com/problems/insert-interval/
#
# Problem Summary:
# You are given a list of non-overlapping intervals sorted by start time.
# Insert a new interval and merge if necessary.
#
# Example:
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# -----------------------------------------------------
# Core Idea:
# We divide the problem into 3 logical phases:
#
# 1️⃣ Add all intervals completely BEFORE newInterval
#    (no overlap)
#
# 2️⃣ Merge all overlapping intervals with newInterval
#    Expand newInterval boundaries while overlapping.
#
# 3️⃣ Add remaining intervals AFTER merged interval
#
# -----------------------------------------------------
# Why This Works:
#
# Since intervals are already sorted and non-overlapping:
# - All non-overlapping left intervals come first
# - Then overlapping block (if any)
# - Then right-side intervals
#
# So a single pass O(n) solution works.
#
# -----------------------------------------------------
# Time Complexity:
# O(n)
#
# Space Complexity:
# O(n) for result list
#
# -----------------------------------------------------
# Code Walkthrough:
#
# while intervals[i][1] < newInterval[0]:
#    → current interval ends before newInterval starts
#      → no overlap → just append
#
# while intervals[i][0] <= newInterval[1]:
#    → intervals overlap
#      → expand newInterval boundaries
#
# Finally append newInterval (merged result)
# Then append remaining intervals.
