# LeetCode 67
# Problem: Add Binary
# Link: https://leetcode.com/problems/add-binary/
#
# Approach:
# Convert both binary strings into integers using base-2 conversion.
# Add the two integer values.
# Convert the resulting sum back into a binary string using Python's format function.
#
# Steps:
# 1. int(a, 2) converts binary string 'a' to decimal integer.
# 2. int(b, 2) converts binary string 'b' to decimal integer.
# 3. Add both integers.
# 4. format(z, 'b') converts the integer sum back to binary string.
#
# Note:
# This is a Python built-in shortcut approach.
# Interviewers may expect a manual binary addition implementation
# (handling carry from right to left).
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y = int(a,2),int(b,2)
        z = x+y
        return format(z,'b')  
    
#interview version 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])
