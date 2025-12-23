# LeetCode 168 - Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
#
# Approach:
# This problem follows a modified base-26 conversion where there is no zero.
# Repeatedly subtract 1 from the column number, take modulo 26 to get the
# corresponding character, and divide the number by 26.
# Build the result string from right to left.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26

        return result
