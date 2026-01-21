# LeetCode 202: Happy Number
# https://leetcode.com/problems/happy-number/
#
# Approach:
# Repeatedly replace the number with the sum of the squares of its digits.
# If the process eventually reaches 1, the number is happy.
#
# If the number is not happy, the sequence will fall into a cycle.
# To detect this cycle, a set is used to keep track of numbers that
# have already been seen.
#
# Steps:
# 1. While n is not 1:
#    - If n has been seen before, a cycle exists → return False.
#    - Add n to the seen set.
#    - Compute the sum of squares of digits of n.
#    - Update n with this sum.
# 2. If n becomes 1, return True.
#
# Time Complexity: O(log n) per iteration (digits processing)
# Space Complexity: O(log n) due to the seen set
