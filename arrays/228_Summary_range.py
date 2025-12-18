# LeetCode 228 - Summary Ranges
#
# Approach:
# Iterate through the sorted array while tracking the start of a consecutive range.
# When the current number is not consecutive to the previous one, close the range
# by checking if it is a single number or a range, then store it.
# After the loop, handle the final range separately.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output list)
