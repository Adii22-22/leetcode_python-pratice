# LeetCode 415 - Add Strings
# https://leetcode.com/problems/add-strings/
#
# Approach:
# Use two pointers starting from the end of both strings.
# Add corresponding digits along with a carry value.
# Append the current digit (total % 10) to the result list.
# Continue while any digits remain or carry is non-zero.
# Reverse the result at the end and join to form the final string.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) -1
        p2 = len(num2) -1
        carry = 0
        result = []
        while p1>=0 or p2>=0  or carry >0:
            digit1 = int(num1[p1]) if p1>=0 else 0
            digit2 = int(num2[p2]) if p2>=0 else 0
            total = digit1 + digit2 + carry
            result.append(str(total%10))
            carry = (total//10)
            p1-=1
            p2-=1
        result.reverse()
        return "".join(result)