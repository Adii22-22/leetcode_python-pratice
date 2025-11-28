# LeetCode 414: Third Maximum Number (O(n) Optimal Approach)
# Date solved: Nov 27, 2025
# Approach: Track Top 3 Distinct Maximums in One Pass
# Explanation:
#   Maintain three variables (first, second, third) representing the top three
#   distinct maximum values. Skip duplicates before updating. For each number:
#   update first, second, or third accordingly using a single pass.
#   If fewer than 3 distinct values exist, return the maximum (first).
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int: # type: ignore
        first = None
        second = None
        third = None
        for n in nums:
            if n == first or n == second or n== third:
                continue

            if first is None or n > first:
                third = second
                second = first
                first = n
            elif second is None or n > second:
                third = second 
                second = n
            elif third is None or n >third:
               third = n

        if third == None:
            return first
        else:
            return third
        