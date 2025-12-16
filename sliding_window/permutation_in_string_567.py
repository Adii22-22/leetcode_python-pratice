"""
LeetCode 567 - Permutation in String

Approach:
- Use sliding window of size len(s1).
- Maintain frequency maps for s1 and current window in s2.
- Track how many characters match required frequency.
- If all required characters match, permutation exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""
