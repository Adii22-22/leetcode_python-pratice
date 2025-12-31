# LeetCode 128 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Approach:
# Use a set for O(1) lookups.
# For each number, check if it is the start of a sequence
# (i.e., number - 1 does not exist in the set).
# From each start, walk forward (number + 1, number + 2, ...)
# and count the length of the consecutive sequence.
# Track and return the maximum length found.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # type: ignore
        numbers = set(nums)
        max_len = 0
        sequence =0
        current = 0
        for num in numbers:
            if (num-1) not in numbers:
                sequence = 1
                current = num
                while current+1 in numbers:
                    current+=1
                    sequence+=1
                max_len = max(max_len,sequence)
        return max_len