# LeetCode 762
# Problem: Prime Number of Set Bits in Binary Representation
# Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
#
# Problem Summary:
# For every number in range [left, right],
# count how many numbers have a PRIME number of set bits (1s)
# in their binary representation.
#
# Example:
# 6  -> 110  -> 2 set bits (prime)
# 7  -> 111  -> 3 set bits (prime)
# 8  -> 1000 -> 1 set bit (not prime)
#
# ---------------------------------------------------------
# Approach:
#
# 1. Predefine a set of prime numbers.
#    Since max number ≤ 10^6,
#    maximum set bits ≤ 20 (actually ≤ 32 for safety).
#
# 2. For each number in range:
#       - Use number.bit_count() to count 1s.
#       - If that count is in the prime set,
#         increment the answer.
#
# 3. Return total count.
#
# ---------------------------------------------------------
# Why This Works:
#
# - bit_count() runs in O(1).
# - Prime lookup in a set is O(1).
# - Overall complexity is linear in range size.
#
# ---------------------------------------------------------
# Time Complexity:
# O(n)  where n = right - left
#
# Space Complexity:
# O(1)  (prime set size is constant)
#
# ---------------------------------------------------------
# Note:
# Using a precomputed prime set is faster than
# checking primality every time.

import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2,3,5,7,11,13,17,19,23,29,31}
        prime_number = 0
        for number in range(left,right+1):
            if number.bit_count() in primes:
                prime_number +=1
        return prime_number
    

#SUBOPTIMAL SOLUTION => O((R−L)∗Sqrt(Log(R)))
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_number = 0
        def isprime(num):
            if num <=1: return False
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0:return False
            return True
        for number in range(left,right+1):
            if isprime(number.bit_count()) == True:
                prime_number+=1
        return prime_number     
    
#bit masking 
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(1 for i in range(left, right + 1) if (665772 >> i.bit_count()) & 1)