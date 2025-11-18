# ------------------------------------------------------------
# LeetCode 349: Intersection of Two Arrays
# Difficulty: Easy
# Date Solved: Nov 18, 2025
#
# Approach:
# - Convert nums1 into a set to enable O(1) lookup time.
# - Iterate through nums2 and check which elements appear in the set.
# - Add matches into a new set `result` to avoid duplicates.
# - Convert result back to a list before returning.
#
# Key Insight:
# - Using sets ensures the solution is efficient and automatically
#   handles duplicate values without extra logic.
#
# Time Complexity: O(n + m)
#   - Building the first set takes O(n)
#   - Iterating through the second list takes O(m)
#
# Space Complexity: O(n)
#   - For storing the set of unique elements from nums1
# ------------------------------------------------------------
# ------------------------------------------------------------
# LeetCode 349: Intersection of Two Arrays
# Difficulty: Easy
# Date Solved: Nov 18, 2025
#
# Approach:
# - Convert nums1 into a set to enable O(1) lookup time.
# - Iterate through nums2 and check which elements appear in the set.
# - Add matches into a new set `result` to avoid duplicates.
# - Convert result back to a list before returning.
#
# Key Insight:
# - Using sets ensures the solution is efficient and automatically
#   handles duplicate values without extra logic.
#
# Time Complexity: O(n + m)
#   - Building the first set takes O(n)
#   - Iterating through the second list takes O(m)
#
# Space Complexity: O(n)
#   - For storing the set of unique elements from nums1
# ------------------------------------------------------------
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
        x = set(nums1)
        result = set()
        for num in nums2:
            if num in x:
                result.add(num)
        result = list(result)
        return result
        
