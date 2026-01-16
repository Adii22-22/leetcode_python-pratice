# LeetCode 541: Reverse String II
# https://leetcode.com/problems/reverse-string-ii/
#
# Approach:
# The string is processed in blocks of size 2k.
# For every such block, only the first k characters are reversed,
# while the remaining k characters (if present) are left unchanged.
#
# Steps:
# 1. Convert the string into a list to allow in-place modification.
# 2. Iterate through the string in steps of 2k.
# 3. For each block, reverse characters from index i to min(i + k - 1, end of string)
#    using a two-pointer approach.
# 4. After processing all blocks, convert the list back into a string.
#
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(n), due to conversion of string to list
