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
