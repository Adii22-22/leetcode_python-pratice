# LeetCode 844 - Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
#
# Approach:
# Use stacks to process both strings independently.
# Traverse each string character by character:
# - If the character is '#', remove the last character from the stack if it exists.
# - Otherwise, push the character onto the stack.
# After processing both strings, compare the final stacks.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        stack1 = []
        stack2 = []

        for p1 in s:
            if p1 == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(p1)

        for p2 in t:
            if p2 == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(p2)
 
        if stack1 == stack2:
            return True
        else:
            return False