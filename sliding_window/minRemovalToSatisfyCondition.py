# Problem: Minimum Removals to Satisfy max <= min * k
#
# Approach:
# 1. Sort the array so that minimum and maximum values of any subset
#    can be compared using indices.
# 2. Use a sliding window with two pointers (i and j).
# 3. Expand the window by moving j to the right.
# 4. If the condition nums[j] > nums[i] * k is violated, shrink the window
#    by moving i to the right until the condition is restored.
# 5. Track the maximum valid window size found.
#
# The minimum number of removals is the total length of the array minus
# the size of the largest valid window.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int: # type: ignore
        nums.sort()
        n = len(nums)
        i = 0
        max_window = 0

        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1
            max_window = max(max_window, j - i + 1)

        return n - max_window
