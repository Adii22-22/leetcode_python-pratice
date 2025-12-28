# LeetCode 844 - Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
#
# Approach:
# Use stacks to process both strings independently.
# Traverse each string character by character:
# - If the character is '#', remove the last character from the stack if it exists.
# - Otherwise, push the character onto the stack.
# After processing both strings, compare the final stacks.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
