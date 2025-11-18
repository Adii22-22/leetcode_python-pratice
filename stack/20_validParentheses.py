"""
LeetCode Problem: 20. Valid Parentheses
Difficulty: Easy
Solved on: Nov 15, 2025

Approach:
---------
Use a stack to track opening brackets.
Whenever a closing bracket appears, the top of the stack must be the matching opening bracket.
If the stack becomes invalid at any point → return False.
If the entire string is processed and the stack is empty → return True.

Time Complexity:  O(n)
Space Complexity: O(n), for the stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening parentheses
        stack = []

        # Set of opening brackets
        opening = {"(", "[", "{"}

        # Mapping closing bracket → matching opening bracket
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Iterate through each character in the string
        for char in s:
            if char in opening:
                # Push to stack if it's an opening bracket
                stack.append(char)
            else:
                # If closing bracket appears but stack is empty → invalid
                if not stack:
                    return False
                
                # If top of stack doesn't match expected opening → invalid
                if stack[-1] != matching[char]:
                    return False

                # If matched correctly → pop from stack
                stack.pop()

        # If stack is empty → all brackets were matched properly
        return not stack
