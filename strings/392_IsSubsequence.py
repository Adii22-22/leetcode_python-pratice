# --------------------------------------------------------------
# Problem: 392. Is Subsequence
# Difficulty: Easy
# Date Solved: Nov 13, 2025
#
# Approach:
# - Use a two-pointer technique:
#     • Pointer i tracks position in string s (the subsequence).
#     • Pointer j scans through string t (the main string).
# - When characters match, advance both pointers.
# - When they don't match, advance only j.
# - If pointer i reaches the end of s, the entire subsequence was found.
#
# Time Complexity: O(n) — n = len(t), single pass through t.
# Space Complexity: O(1) — constant extra memory.
# --------------------------------------------------------------
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)
