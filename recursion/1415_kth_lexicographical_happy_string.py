# LeetCode 1415
# Problem: The k-th Lexicographical String of All Happy Strings of Length n
# Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
#
# Problem Summary:
# A "happy string" is defined as:
# - Consists only of characters 'a', 'b', 'c'
# - No two adjacent characters are the same
#
# Given integers n and k, return the k-th lexicographically
# smallest happy string of length n.
# If fewer than k such strings exist, return "".
#
# Example:
# n = 3
# Happy strings:
# aba, abc, aca, acb, bab, bac, bca, bcb, cab, cac, cba, cbc
#
# ---------------------------------------------------------
# Approach (Backtracking):
#
# We generate all possible happy strings using recursion.
#
# Steps:
# 1. Start with an empty string.
# 2. Try adding characters 'a', 'b', 'c'.
# 3. Only add a character if it is different from the
#    previous character in the string.
# 4. Continue building until length == n.
# 5. Store each valid happy string in a result list.
#
# Since characters are explored in order ['a','b','c'],
# the generated strings are automatically lexicographically sorted.
#
# After generation:
# - If k is within bounds → return result[k-1]
# - Otherwise → return ""
#
# ---------------------------------------------------------
# Why Backtracking Works:
#
# At each position we have at most 2 valid choices
# (because we cannot repeat the previous character).
#
# Total possible strings ≈ 3 * 2^(n-1)
#
# ---------------------------------------------------------
# Time Complexity:
# O(3 * 2^(n-1))
#
# Space Complexity:
# O(3 * 2^(n-1)) for storing generated strings
#
# ---------------------------------------------------------
# Note:
# A more optimized solution can stop recursion once
# the k-th string is found instead of generating all.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def lexi(lexi_string):
            if len(lexi_string) == n:
                result.append(lexi_string)
                return 
            
            for char in ['a','b','c']:
                if not lexi_string or lexi_string[-1] != char:
                    lexi(lexi_string + char) 
        
        lexi("")
        if len(result) < k:
            return ""
        else:
            return result[k-1]