# LeetCode 191: Number of 1 Bits
# Date solved: Dec 8, 2025
# Approach: Bit Manipulation (Binary Conversion)
# Explanation:
#   Convert the number to binary and count how many '1' bits appear.
#   This effectively measures the Hamming Weight of the integer.
# Time Complexity: O(1)  # 32-bit integer, constant operations
# Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for one in binary:
            if one == "1":
                count += 1
        return count