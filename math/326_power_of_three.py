# LeetCode 326: Power of Three
# Date solved: Dec 2, 2025
# Approach: Math / Repeated Division
# Explanation:
#   A number is a power of three if it can be repeatedly divided by 3 until
#   it becomes 1. First, discard non-positive values. Then divide n by 3
#   while divisible. After the loop, if the result is 1, it was a power of 3.
# Time Complexity: O(log₃ n)
# Space Complexity: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n = n//3
        if n == 1:
                return True
        else:
                return False