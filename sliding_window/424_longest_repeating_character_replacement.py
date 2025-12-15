# LeetCode 424 - Longest Repeating Character Replacement
# Difficulty: Medium
# Topic: Sliding Window + HashMap
#
# Approach:
# Use sliding window with frequency count.
# Track max frequency character in the window.
# Window is valid if (window_size - max_freq) <= k.
# Shrink window from left when replacements exceed k.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  # 26 uppercase letters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) # type: ignore
        max_freq = 0
        max_length = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
                
