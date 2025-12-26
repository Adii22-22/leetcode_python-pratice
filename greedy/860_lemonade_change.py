# LeetCode 860 - Lemonade Change
# https://leetcode.com/problems/lemonade-change/
#
# Approach:
# Use a greedy strategy by tracking the count of $5 and $10 bills.
# For each customer:
# - If the bill is $5, increase the count of $5 bills.
# - If the bill is $10, give one $5 as change if available.
# - If the bill is $20, prefer giving one $10 and one $5 as change;
#   otherwise, give three $5 bills if possible.
# If exact change cannot be provided at any step, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
