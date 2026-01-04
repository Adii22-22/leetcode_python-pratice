# LeetCode 1390: Four Divisors
# https://leetcode.com/problems/four-divisors/
#
# Approach:
# For each number, count its divisors using the fact that divisors come in pairs.
# Loop only from 1 to sqrt(num) (inclusive). Whenever a divisor is found, include
# both the divisor and its paired value (num // d).
#
# Track the number of divisors and their sum simultaneously. If the divisor count
# exceeds 4, stop early since the number is invalid for this problem.
# If a number ends with exactly 4 divisors, add its divisor sum to the total answer.
#
# Time Complexity: O(sum of sqrt(num)) over all numbers
# Space Complexity: O(1)
