# LeetCode 1523: Count Odd Numbers in an Interval Range
# Date solved: Dec 5, 2025
# Approach: Math Formula (O(1))
# Explanation:
#   The count of odd numbers from 1 to x is given by: (x + 1) // 2.
#   Therefore, the number of odd numbers between low and high (inclusive) is:
#       (high + 1) // 2  -  (low // 2)
#   This avoids looping and gives a constant-time solution.
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)// 2 - (low//2)
