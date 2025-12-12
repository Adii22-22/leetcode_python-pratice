# ----------------------------------------------------------
# LeetCode 1189 - Maximum Number of Balloons
# Category: Hashing / Frequency Counting
# Date Solved: 2025-12-12
# Logic:
#   - Count occurrences of each character in the word "balloon".
#   - The word needs: b(1), a(1), l(2), o(2), n(1)
#   - Divide counts of 'l' and 'o' by 2 because they're used twice.
#   - The minimum count among required characters decides the answer.
# ----------------------------------------------------------
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int) # type: ignore

        # Count only relevant letters
        for ch in text:
            if ch in "balloon":
                freq[ch] += 1

        # 'l' and 'o' appear twice in "balloon"
        l = freq['l'] // 2
        o = freq['o'] // 2

        # Return minimum available complete sets
        return min(freq['b'], freq['a'], l, o, freq['n'])