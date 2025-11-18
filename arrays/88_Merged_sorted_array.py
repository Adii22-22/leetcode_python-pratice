# -------------------------------------------------------------
# LeetCode Problem: 88. Merge Sorted Array
# Solved on: Nov 9, 2025
# Difficulty: Easy
# Language: Python
# -------------------------------------------------------------
# Problem Statement:
# You are given two sorted integer arrays nums1 and nums2, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums2 into nums1 as one sorted array in-place.
#
# Example:
# Input: nums1 = [1,2,3,0,0,0], m = 3
#        nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Approach:
# - Use three pointers:
#     p1: end of nums1’s initialized elements (m-1)
#     p2: end of nums2 (n-1)
#     p: end of nums1 total length (m+n-1)
# - Compare from the end and place the larger element at position p.
# - Continue moving backward until all nums2 elements are placed.
#
# Time Complexity: O(m + n)
# Space Complexity: O(1)
# -------------------------------------------------------------

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: # type: ignore
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
