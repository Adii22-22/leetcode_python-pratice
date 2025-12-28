# LeetCode 415 - Add Strings
# https://leetcode.com/problems/add-strings/
#
# Approach:
# Use two pointers starting from the end of both strings.
# Add corresponding digits along with a carry value.
# Append the current digit (total % 10) to the result list.
# Continue while any digits remain or carry is non-zero.
# Reverse the result at the end and join to form the final string.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
