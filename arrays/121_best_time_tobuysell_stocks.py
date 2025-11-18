# -------------------------------------------------------------
# LeetCode Problem: 121. Best Time to Buy and Sell Stock
# Solved on: Nov 7, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.
# Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.
#
# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
#
# Approach:
# - Use a single-pass method while tracking:
#     1. The minimum price so far (`min_price`)
#     2. The maximum profit so far (`max_profit`)
# - For each price:
#     - Update `min_price` if a smaller price is found.
#     - Calculate profit = current price - min_price.
#     - Update `max_profit` if this profit is higher.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:    # pyright: ignore[reportUndefinedVariable]
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
