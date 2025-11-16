# ---------------------------------------------------------------
# LeetCode 242: Valid Anagram
# Difficulty: Easy
# Solved on: Nov 2, 2025
# and tried again on nov 16 using hash map and this hash version
# Approach:
# Use a hash map (dictionary) to count character frequencies.
# 1. Count each character in string s.
# 2. Subtract counts for each character in string t.
# 3. If all counts return to zero, the strings are anagrams.
#
# Time Complexity: O(n) – iterate through both strings once
# Space Complexity: O(n) – dictionary stores character counts
# ---------------------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        # Count frequency of characters in s
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        # Decrease frequency for characters seen in t
        for char in t:
            if char in dict:
                dict[char] -= 1
            else:
                return False   # t has a char not in s → not an anagram

        # All character counts must return to zero
        for char in dict:
            if dict[char] != 0:
                return False

        return True
