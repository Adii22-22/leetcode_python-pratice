# -------------------------------------------------------------
# LeetCode Problem: 205. Isomorphic Strings
# Solved on: Dec 11, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Two strings s and t are isomorphic if the characters in s can be replaced
# to get t, maintaining the order. Each character must map to exactly one
# character, and no two characters can map to the same one.
#
# Example:
# s = "egg", t = "add" -> True
# s = "foo", t = "bar" -> False
#
# Approach:
# Maintain two dictionaries:
#   - s -> t mapping
#   - t -> s mapping
# For each index, check if the mappings already exist and match.
# If not, reject. Otherwise create new mapping.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  # bounded by character set size
# -------------------------------------------------------------
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictt_st = {}
        dictt_ts = {}
        for i in range(len(s)):
            if s[i] in dictt_st:
                if dictt_st[s[i]] != t[i]:
                    return False
            else:
                dictt_st[s[i]] = t[i]
            

            if t[i] in dictt_ts:
                if dictt_ts[t[i]] != s[i]:
                    return False
            else:
                dictt_ts[t[i]] = s[i]

        return True
