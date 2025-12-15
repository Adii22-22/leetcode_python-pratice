# LeetCode 409 - Longest Palindrome
# Difficulty: Easy
# Topic: HashMap /Sliding window/ Greedy
#
# Approach:
# Count frequency of each character.
# Use all even counts fully.
# From odd counts, use (count - 1).
# If any odd count exists, place one character in the center.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
