# LeetCode 1653
# Problem: Minimum Deletions to Make String Balanced
# Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
#
# Approach:
# A string is balanced if all 'a' characters appear before any 'b' characters.
# This means we must eliminate any pattern where a 'b' appears before an 'a'.
#
# We scan the string from left to right and track:
# - b_count: number of 'b' characters seen so far
# - deletions: minimum deletions needed so far to keep the string balanced
#
# When we see:
# - 'b': it is always safe, so we increment b_count
# - 'a' after one or more 'b's: this creates a conflict
#   We choose the cheaper option:
#   1) delete this 'a'  -> deletions + 1
#   2) delete all previous 'b's -> b_count
#   and keep the minimum of the two
#
# This greedy choice works because each conflict is resolved optimally
# using only prefix information.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                b_count +=1
            else:
                if b_count > 0: 
                    deletions = min(deletions+1,b_count)
        return deletions     