# Solved on Nov 23, 2025
# LeetCode 1672: Richest Customer Wealth
# Difficulty: Easy
#
# Problem Summary:
# Given a 2D list 'accounts', where accounts[i] represents the wealth of the i-th customer 
# across multiple bank accounts, find the customer with the maximum total wealth.
#
# Approach:
# - For each customer, compute the sum of their accounts.
# - Track all sums or directly track the maximum.
# - Return the maximum wealth value.
#
# Time Complexity: O(n * m) 
#   where n = number of customers, m = number of accounts per customer.
# Space Complexity: O(n) due to storing customer wealth (or O(1) if using direct max tracking).
