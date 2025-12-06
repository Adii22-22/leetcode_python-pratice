# LeetCode 1480: Running Sum of 1D Array
# Date solved: Dec 6, 2025
# Approach: Prefix Sum
# Explanation:
#   Maintain a running total while iterating through the list.
#   Each new value in the result represents the cumulative sum up to that index.
#   This is a classic prefix sum calculation completed in a single pass.
# Time Complexity: O(n)
# Space Complexity: O(1) extra (excluding the output list)
class Solution: 
    def runningSum(self, nums: List[int]) -> List[int]:  # type: ignore
        prefix = [] 
        current_sum = 0 
        for num in nums: 
            current_sum += num 
            prefix.append(current_sum) 
        return prefix