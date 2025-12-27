# LeetCode 345 - Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/
#
# Approach:
# Use two pointers starting from the beginning and end of the string.
# Move the left pointer forward until a vowel is found.
# Move the right pointer backward until a vowel is found.
# Swap the vowels at both pointers and move both pointers inward.
# Continue until the pointers cross, then join the list into a string.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1
        s_list = list(s)
        vowel = {"a","A", "e","E","i","I","o","O","u","U"}
        while p1 <= p2:
            if s_list[p1] not in vowel:
                p1+=1
            elif s_list[p2] not in vowel:
                p2-=1
            else:
                s_list[p1],s_list[p2] = s_list[p2],s_list[p1]
                p1+=1
                p2-=1
        return "".join(s_list)