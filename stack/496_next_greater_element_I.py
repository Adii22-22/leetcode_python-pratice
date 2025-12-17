"""
LeetCode 496 – Next Greater Element I
Difficulty: Easy
Topic: Stack (Monotonic Stack)

Approach:
- Use a monotonic decreasing stack to process nums2.
- Traverse nums2 and resolve the next greater element for each number.
- Store results in a hashmap where:
    key   -> number from nums2
    value -> its next greater element
- If no greater element exists, map it to -1.
- Build the final result by looking up values for nums1.

Why Stack:
- Each element is pushed and popped at most once.
- Ensures O(n) time complexity.

Time Complexity: O(n)
Space Complexity: O(n)

Status: Accepted ✅
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
        next_greater = {}
        stack = []
        n = len(nums2)

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                next_greater[nums2[index]] = nums2[i]      
            stack.append(i)
        
        for i in stack:
            next_greater[nums2[i]] = -1

        return [next_greater[x] for x in nums1]