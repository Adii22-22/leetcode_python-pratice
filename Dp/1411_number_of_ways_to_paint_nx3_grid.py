# LeetCode 1411: Number of Ways to Paint N × 3 Grid
# https://leetcode.com/problems/number-of-ways-to-paint-nx3-grid/
#
# Approach:
# Instead of treating this as a full grid DP, observe that each row of 3 cells
# can form only two valid color patterns under adjacency constraints:
# 1) ABA: first and third cells have the same color, middle is different
# 2) ABC: all three cells have different colors
#
# For the first row, both patterns have 6 valid combinations each.
# For every next row, the number of valid ways depends only on the previous row:
# - A new ABA row can be formed from previous ABA or ABC rows using fixed transitions
# - A new ABC row can also be formed from previous ABA or ABC rows using fixed transitions
#
# We iteratively update the counts of ABA and ABC patterns row by row without
# storing a full DP table, keeping only the previous counts.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 +7

        aba = 6
        abc = 6

        for _ in range(n-1):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD

            aba = next_aba
            abc = next_abc
        return (aba+abc) % MOD