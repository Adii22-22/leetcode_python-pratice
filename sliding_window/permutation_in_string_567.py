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
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1dict = defaultdict(int) # type: ignore
        s2dict = defaultdict(int) # type: ignore

        for char in s1:
            s1dict[char] += 1

        required = len(s1dict)
        formed = 0
        l = 0

        for r in range(len(s2)):
            char = s2[r]
            s2dict[char] += 1

            if char in s1dict and s2dict[char] == s1dict[char]:
                formed += 1

            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in s1dict and s2dict[left_char] == s1dict[left_char]:
                    formed -= 1
                s2dict[left_char] -= 1
                l += 1

            if formed == required:
                return True

        return False
