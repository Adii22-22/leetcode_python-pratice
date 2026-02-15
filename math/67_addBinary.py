# LeetCode 67
# Problem: Add Binary
# Link: https://leetcode.com/problems/add-binary/
#
# Approach:
# Convert both binary strings into integers using base-2 conversion.
# Add the two integer values.
# Convert the resulting sum back into a binary string using Python's format function.
#
# Steps:
# 1. int(a, 2) converts binary string 'a' to decimal integer.
# 2. int(b, 2) converts binary string 'b' to decimal integer.
# 3. Add both integers.
# 4. format(z, 'b') converts the integer sum back to binary string.
#
# Note:
# This is a Python built-in shortcut approach.
# Interviewers may expect a manual binary addition implementation
# (handling carry from right to left).
#
# Time Complexity: O(n)
# Space Complexity: O(n)
