# LeetCode 258: Add Digits
# Date solved: Nov 30, 2025
# Approach: Math / Digital Root
# Explanation:
#   Uses the digital root formula. Any positive number reduces to
#   1 + (num - 1) % 9. Zero returns 0. Avoids loops and repeated summing.
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9