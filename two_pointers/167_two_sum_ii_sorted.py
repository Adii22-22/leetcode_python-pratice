# -------------------------------------------------------------
# LeetCode Problem: 167. Two Sum II - Input Array Is Sorted
# Solved on: Dec 10, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given a sorted array of integers and a target value, return the
# 1-indexed positions of the two numbers such that they add up to
# the target. Each input has exactly one solution.
#
# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Approach:
# Use the two-pointer technique.
# - Start with one pointer at the left end and one at the right.
# - If the sum is too large, move the right pointer left.
# - If the sum is too small, move the left pointer right.
# - When the sum equals the target, return indices.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------

