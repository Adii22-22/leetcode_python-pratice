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
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)

        for i in range(0,len(l),2*k):
            left = i
            right = min(i+k-1,len(l)-1)

            while left < right:
                l[left],l[right] = l[right],l[left]
                left +=1
                right -= 1

        return "".join(l)
