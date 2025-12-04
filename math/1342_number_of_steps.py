# LeetCode 1342: Number of Steps to Reduce a Number to Zero
# Date solved: Dec 4, 2025
# Approach: Simulation / Bit Logic
# Explanation:
#   If the number is even, divide it by 2 (one operation). If the number is odd,
#   subtract 1 (one operation). Repeat this process until the number becomes 0.
#   This directly follows the rules given in the problem.
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                count +=1
            elif num % 2 == 1:
                num = (num - 1) 
                count +=1

        return count
        
        