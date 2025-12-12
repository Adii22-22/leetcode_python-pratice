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