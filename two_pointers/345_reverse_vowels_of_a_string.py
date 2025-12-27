# LeetCode 345 - Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/
#
# Approach:
# Use two pointers starting from the beginning and end of the string.
# Move the left pointer forward until a vowel is found.
# Move the right pointer backward until a vowel is found.
# Swap the vowels at both pointers and move both pointers inward.
# Continue until the pointers cross, then join the list into a string.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
