# LeetCode 389 - Find the Difference
# https://leetcode.com/problems/find-the-difference/
#
# Approach:
# Use a hash map (dictionary) to count character frequencies.
# First, count all characters in string t.
# Then subtract counts using characters from string s.
# The character with remaining count equal to 1 is the extra character.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dict = defaultdict(int) # type: ignore
        for i in t:
            t_dict[i] += 1

        for i in s:
            if i in t_dict:
                t_dict[i] -= 1

        for char in t_dict:
            if t_dict[char] == 1:
                return char