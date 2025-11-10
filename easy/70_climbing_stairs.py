# -------------------------------------------------------------
# LeetCode Problem: 70. Climbing Stairs
# Solved on: Nov 8, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?
#
# Example:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top:
# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step
#
# Approach:
# This is a Fibonacci-style problem where:
# ways(n) = ways(n - 1) + ways(n - 2)
# Use recursion with memoization to avoid redundant computations:
# - Store previously computed results in a cache (dictionary)
# - Base cases: if n == 1 → 1 way, if n == 2 → 2 ways
# - Return cached results when available
#
# Time Complexity: O(n)    # Each subproblem computed once
# Space Complexity: O(n)   # Recursion stack + cache
# -------------------------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(k):
            if k in cache:
                return cache[k]
            if k == 1: return 1
            if k == 2: return 2
            result = helper(k - 1) + helper(k - 2)
            cache[k] = result
            return result

        return helper(n)
