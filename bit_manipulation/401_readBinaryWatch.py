# LeetCode 401
# Problem: Binary Watch
# Link: https://leetcode.com/problems/binary-watch/
#
# Approach (Brute Force + Bit Counting):
#
# A binary watch represents:
# - Hours using 4 LEDs (0 to 11)
# - Minutes using 6 LEDs (0 to 59)
#
# We iterate through all valid times:
#   - hour: 0 → 11
#   - minute: 0 → 59
#
# For each time:
#   - Count number of 1-bits in hour using bit_count()
#   - Count number of 1-bits in minute using bit_count()
#   - If total LEDs ON equals turnedOn, include that time
#
# Formatting:
# - Minutes must always be 2 digits (e.g., 3 → "03")
#
# Key Insight:
# Instead of generating LED combinations directly,
# we generate all valid times and filter using bit counts.
#
# Time Complexity:
# O(12 × 60) = O(1)
# (Always 720 iterations — constant)
#
# Space Complexity:
# O(k), where k is number of valid times returned
#
# This is clean, simple, and interview-acceptable.
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]: # type: ignore
        times = []
        for i in range(12):
            for j in range(60):
                x = i.bit_count()
                y = j.bit_count()
                if x+y == turnedOn:
                    if j < 10:
                        times.append(f"{i}:0{j}")
                    else:
                        times.append(f"{i}:{j}")
        return times    