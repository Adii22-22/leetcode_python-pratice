# -------------------------------------------------------------------------------
# LeetCode 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Date Solved: Nov 14, 2025
#
# Approach: Sliding Window + HashSet
#
# - Use two pointers: `start_win` (left) and `end_win` (right) to form a window.
# - Use a Set (`substring_char`) to store characters in the current window.
#
# Sliding Window Logic:
#   • Expand the window by moving `end_win`.
#   • If the current char is not in the Set → Add it and update max length.
#   • If the char already exists → Shrink the window from the left by removing
#     characters until the duplicate is removed.
#
# Why This Works:
# - The window always contains unique characters.
# - Each character is added/removed at most once → O(n) efficient solution.
#
# Time Complexity:  O(n)  — each pointer moves at most n steps  
# Space Complexity: O(k)  — size of hash set (k = unique characters)
# -------------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            start_win = 0
            end_win = 0
            max_len = 0
            substring_char = set()
            while end_win < len(s):
                if s[end_win] not in substring_char:
                    substring_char.add(s[end_win])
                    end_win +=1
                    window_len = end_win - start_win
                    max_len = max(max_len,window_len)
                else:
                    while s[end_win] in substring_char:
                        substring_char.remove(s[start_win])
                        start_win +=1
                    
            return max_len
