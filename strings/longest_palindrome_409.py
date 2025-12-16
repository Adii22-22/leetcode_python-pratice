"""
LeetCode 409 - Longest Palindrome

Approach:
- Count frequency of each character.
- Use all even counts fully.
- For odd counts, use (count - 1).
- If any odd count exists, place one character in the center.

Time Complexity: O(n)
Space Complexity: O(1)  # fixed alphabet
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = defaultdict(int) # type: ignore
        for char in s:
            frequency[char]+= 1

        length = 0
        odd_found = False
        for count in frequency.values():
            if count % 2 ==0:
                length += count
            else:
                length += count - 1
                odd_found = True
            
        if odd_found:
            length +=1

        return length