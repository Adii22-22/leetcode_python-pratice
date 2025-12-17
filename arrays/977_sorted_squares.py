"""
LeetCode 977 — Squares of a Sorted Array

Approach:
Used two-pointer technique starting from both ends of the array.
Compared absolute values, placed the larger square at the end of result array.
Moved pointers accordingly and filled the result array from right to left.

Time Complexity: O(n)
Space Complexity: O(n)

Concepts Used:
- Two pointers
- Absolute value comparison
- Array traversal
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: # type: ignore
        n = len(nums)
        res = [None] * n
        left = 0
        right = n - 1
        pos = n -1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left] * nums[left]
                res[pos] = square
                left+=1
            else:
                square =nums[right] * nums[right]
                res[pos] = square
                right -= 1
            
            pos -= 1

        return res