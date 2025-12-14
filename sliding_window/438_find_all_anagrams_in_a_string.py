# -------------------------------------------------------------
# LeetCode Problem: 438. Find All Anagrams in a String
# Difficulty: Medium
# Pattern: Sliding Window + Hash Map
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given two strings s and p, return all start indices of p's
# anagrams in s.
#
# Approach:
# Use a sliding window of size len(p).
# Maintain two hash maps:
# - need: frequency of characters in p
# - window: frequency of current window in s
# Slide the window and compare maps.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: # type: ignore
        need = defaultdict(int) # type: ignore
        window = defaultdict(int) # type: ignore
        window_lenth = len(p)
        res = []
        l = 0

        for char in p:
            need[char] += 1

        for r in range(0,len(s)):
            window[s[r]] +=1

            if r-l + 1 > len(p):
                left_char = s[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l +=1

            if window == need:
                res.append(l)
        return res
