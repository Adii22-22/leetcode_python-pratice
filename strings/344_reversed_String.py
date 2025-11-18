# --------------------------------------------------------------
# Problem: 344. Reverse String
# Difficulty: Easy
# Date Solved: Nov 10, 2025
#
# Approach:
# - Use a two-pointer technique to reverse the characters in-place.
# - One pointer starts at the beginning (p1), and the other at the end (p2).
# - Swap the characters at these pointers and move them towards each other.
# - Continue until both pointers meet or cross.
#
# Time Complexity: O(n) — each element is visited once.
# Space Complexity: O(1) — in-place modification.
# --------------------------------------------------------------
class Solution:
    def reverseString(self, s: List[str]) -> None: # type: ignore
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            p1 += 1
            p2 -= 1
