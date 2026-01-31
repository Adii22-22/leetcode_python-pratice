# LeetCode 744
# Problem: Find Smallest Letter Greater Than Target
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#
# Approach:
# The letters array is sorted, so we apply binary search.
#
# We search for the smallest character that is strictly greater than target.
# If such a character exists, we keep updating the answer and move left
# to find a smaller valid character.
#
# If no character is greater than target, the problem requires wrap-around,
# so we return letters[0].
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str: # type: ignore
        l, r = 0, len(letters) - 1
        ans = letters[0]

        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1

        return ans
