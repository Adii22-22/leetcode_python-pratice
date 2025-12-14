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
