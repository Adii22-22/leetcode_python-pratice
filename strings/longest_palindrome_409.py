"""
LeetCode 409 - Longest Palindrome

Approach:
- Count frequency of each character.
- Use all even counts fully.
- For odd counts, use (count - 1).
- If any odd count exists, place one character in the center.

Time Complexity: O(n)
Space Complexity: O(1)  # fixed alphabet
"""
