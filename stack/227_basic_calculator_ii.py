# LeetCode 227: Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
#
# Approach:
# Use a single stack to evaluate the expression while scanning it from
# left to right. Keep track of the current number being formed and the
# previous operator.
#
# When an operator is encountered (or end of string is reached),
# apply the previous operator to the current number:
# - '+' : push the number to the stack
# - '-' : push the negative of the number
# - '*' : pop the last number, multiply, and push the result
# - '/' : pop the last number, divide, and push the result
#
# This works because multiplication and division are resolved immediately,
# while addition and subtraction are deferred by pushing values to the stack.
#
# The final result is the sum of all values in the stack.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        prev_op = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(current_num)
                elif prev_op == '-':
                    stack.append(-current_num)
                elif prev_op == '*':
                    stack.append(stack.pop() * current_num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / current_num))

                prev_op = ch
                current_num = 0

        return sum(stack)

