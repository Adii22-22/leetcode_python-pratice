# LeetCode 704: Binary Search
# Date solved: Dec 8, 2025
# Approach: Binary Search (Two Pointers)
# Explanation:
#   Use left and right pointers to repeatedly check the midpoint.
#   Narrow the search range by comparing mid-value with the target.
#   Returns index if found, otherwise returns -1.
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1