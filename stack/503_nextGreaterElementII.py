# LeetCode 503
# Problem: Next Greater Element II
# Link: https://leetcode.com/problems/next-greater-element-ii/
#
# Approach:
# Use a monotonic decreasing stack that stores indices of elements whose
# next greater element has not been found yet.
#
# Since the array is circular, iterate over the array twice (0 to 2*n - 1)
# and access elements using index modulo n.
#
# For each element:
# - While the stack is not empty and the current element is greater than
#   the element at the index on top of the stack, pop that index and set
#   its next greater element in the result array.
#
# - Push indices into the stack only during the first pass (i < n) to avoid
#   infinite looping and duplicate entries.
#
# Elements that never find a greater element remain as -1 in the result.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]: # type: ignore
        n = len(nums)
        stack = []
        res = [-1] * n 

        for i in range(2*n):
            current = nums[i%n]
            while stack and current > nums[stack[-1]]:
                j = stack.pop()
                res[j] = current
            if i < n:
                stack.append(i)
        return res