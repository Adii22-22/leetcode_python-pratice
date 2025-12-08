# LeetCode 1925: Count Square Sum Triples
# Date solved: Dec 8, 2025
# Approach: Brute Force with Pythagorean Check
# Explanation:
#   For every a and b from 1 to n, compute c² = a² + b².
#   If sqrt(c²) is an integer and <= n, count the triple.
#   Order matters (a, b) and (b, a) are counted separately.
# Time Complexity: O(n²)
# Space Complexity: O(1)
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n+1):
            for b in range(1,n+1):
                c2 = a*a + b*b
                c = int(sqrt(c2))
                if c*c == c2 and c <=n:
                    count +=1
        return count