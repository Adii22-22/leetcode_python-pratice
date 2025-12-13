# -------------------------------------------------------------
# LeetCode Problem: 290. Word Pattern
# Solved on: Dec 13, 2025
# Difficulty: Easy
# Language: Python
# Pattern: Hashing / Two-way Mapping
# -------------------------------------------------------------
# Problem Statement:
# Given a pattern and a string s, determine if s follows the same
# pattern. Each letter in the pattern must map to exactly one word,
# and each word must map to exactly one letter.
#
# Example:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: True
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: False
#
# Approach:
# 1. Split the string into words.
# 2. Use two hash maps:
#    - word -> pattern character
#    - pattern character -> word
# 3. Ensure both mappings remain consistent.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
