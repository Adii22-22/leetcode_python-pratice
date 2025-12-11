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
