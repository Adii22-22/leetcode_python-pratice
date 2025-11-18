# ------------------------------------------------------------
# LeetCode 75: Sort Colors
# Difficulty: Medium
# Date Solved: Nov 11, 2025
#
# Approach:
# - Used the Dutch National Flag Algorithm (Three-Pointer approach)
# - Maintains three regions:
#     0s at the beginning (low pointer)
#     1s in the middle (mid pointer)
#     2s at the end (high pointer)
# - Traverse the array with `mid`:
#     - If nums[mid] == 0 → swap with nums[low], move both low & mid
#     - If nums[mid] == 1 → just move mid
#     - If nums[mid] == 2 → swap with nums[high], move high backward
# - Ensures sorting in a single pass O(n) and constant extra space O(1)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None: # type: ignore
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high],nums[mid] = nums[mid],nums[high]
                high -= 1
            else:
                mid += 1