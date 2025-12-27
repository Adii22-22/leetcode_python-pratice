# LeetCode 1768 - Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/
#
# Approach:
# Use two pointers to traverse both strings simultaneously.
# Append characters alternately from each string while both pointers are valid.
# Once one string is exhausted, append the remaining substring of the other string.
# Join the collected characters to form the final merged string.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = []
        p1 = 0
        p2 = 0
        while p1 <len(word1) and p2 < len(word2):
                merge_string.append(word1[p1])
                merge_string.append(word2[p2])
                p1+=1
                p2+=1  
        if p1 < len(word1):
            merge_string.append(word1[p1:]) 
        elif p2 < len(word2):
            merge_string.append(word2[p2:])

        return "".join(merge_string) 