# -------------------------------------------------------------
# LeetCode Problem: 383. Ransom Note
# Difficulty: Easy
# Pattern: Hash Map / Frequency Counting
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed using the letters from magazine.
# Each letter in magazine can only be used once.
#
# Approach:
# Count frequency of each character in magazine.
# For each character in ransomNote, reduce its count.
# If any character is missing or count becomes negative, return False.
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)  (only lowercase letters)
# -------------------------------------------------------------
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mr = defaultdict(int) # type: ignore
        if len(magazine) < len(ransomNote):
            return False
        
        for char in magazine:
            dict_mr[char] += 1
        
        for char in ransomNote:
            if char not in dict_mr or dict_mr[char] == 0:
                return False
            dict_mr[char] -= 1
        
        return True
