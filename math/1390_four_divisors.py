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
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int: # type: ignore
        total_sum = 0
        for num in nums:
            divisors_count = 0
            divisors_sum = 0

            for d in range(1,int(math.sqrt(num)+1)):
                if num%d == 0:
                    other = num//d

                    if d == other:
                        divisors_count +=1
                        divisors_sum += other
                    else:
                        divisors_count+=2
                        divisors_sum += d+other
                    
                    if divisors_count > 4:
                        break

            if divisors_count ==4:
                total_sum += divisors_sum

        return total_sum