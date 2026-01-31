# LeetCode 744
# Problem: Find Smallest Letter Greater Than Target
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#
# Approach:
# The letters array is sorted, so we apply binary search.
#
# We search for the smallest character that is strictly greater than target.
# If such a character exists, we keep updating the answer and move left
# to find a smaller valid character.
#
# If no character is greater than target, the problem requires wrap-around,
# so we return letters[0].
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
