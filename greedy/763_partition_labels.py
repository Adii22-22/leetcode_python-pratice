# LeetCode 763: Partition Labels
# https://leetcode.com/problems/partition-labels/
#
# Approach:
# First, store the last occurrence index of every character in the string.
# This tells how far a partition must extend to fully include a character.
#
# Traverse the string from left to right while maintaining a pointer `end`
# that represents the farthest index the current partition must reach.
# For each character, update `end` using its last occurrence.
#
# When the current index `i` becomes equal to `end`, it means all characters
# seen so far will not appear again later, so a partition can safely be made.
# The partition length is calculated using the current index and a `start`
# pointer, which is then updated for the next partition.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  (bounded by fixed alphabet size)
class Solution:
    def partitionLabels(self, s: str) -> List[int]: # type: ignore
        last_occurance = {}
        end = 0
        start = 0
        cut = []
        for i,ch in enumerate(s):
                last_occurance[ch] = i

        for i in range(len(s)):   
            end = max(end,last_occurance.get(s[i])) 
            if i == end:
                length = i - start + 1
                cut.append(length)
                start = i+1
        return cut