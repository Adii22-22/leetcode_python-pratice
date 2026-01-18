# LeetCode 1895: Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/
#
# Approach:
# A k x k magic square requires:
# - All row sums to be equal
# - All column sums to be equal
# - Both diagonal sums to be equal
#
# To efficiently check sums of rows, columns, and diagonals for any sub-square,
# we precompute prefix sum matrices:
# 1. row prefix sums for fast row sum queries
# 2. column prefix sums for fast column sum queries
# 3. main diagonal (top-left to bottom-right) prefix sums
# 4. anti-diagonal (top-right to bottom-left) prefix sums
#
# Using these prefix sums, each sum query is reduced to O(1).
# We then try all possible square sizes k from 2 up to min(m, n),
# and for each position (i, j), verify whether the k x k square
# satisfies the magic square conditions.
#
# The answer is the maximum k for which a valid magic square exists.
# A 1x1 square is always magic, so the answer starts at 1.
#
# Time Complexity: O(m * n * min(m, n))
# Space Complexity: O(m * n)
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int: # type: ignore
        m, n = len(grid), len(grid[0])
        
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        d1 = [[0]*(n+1) for _ in range(m+1)]
        d2 = [[0]*(n+2) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                d1[i+1][j+1] = d1[i][j] + grid[i][j]
                d2[i+1][j] = d2[i][j+1] + grid[i][j]
        
        def get_row(i, j, k):
            return row[i][j+k] - row[i][j]
        
        def get_col(i, j, k):
            return col[i+k][j] - col[i][j]
        
        def get_d1(i, j, k):
            return d1[i+k][j+k] - d1[i][j]
        
        def get_d2(i, j, k):
            return d2[i+k][j] - d2[i][j+k]
        
        ans = 1
        
        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = get_row(i, j, k)
                    if get_d1(i, j, k) != target or get_d2(i, j, k) != target:
                        continue
                    
                    ok = True
                    for t in range(k):
                        if get_row(i + t, j, k) != target or get_col(i, j + t, k) != target:
                            ok = False
                            break
                    
                    if ok:
                        ans = k
        
        return ans