# LeetCode 424 - Longest Repeating Character Replacement
# Difficulty: Medium
# Topic: Sliding Window + HashMap
#
# Approach:
# Use sliding window with frequency count.
# Track max frequency character in the window.
# Window is valid if (window_size - max_freq) <= k.
# Shrink window from left when replacements exceed k.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  # 26 uppercase letters
