# LeetCode 485: Max Consecutive Ones
# Date solved: Dec 8, 2025
# Approach: Linear Scan / Sliding Window (Implicit)
# Explanation:
#   Traverse the array while counting consecutive 1s.
#   Reset the count when encountering a 0 and track the maximum streak.
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: # type: ignore
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
        return max_count