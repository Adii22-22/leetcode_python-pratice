# LeetCode 1200
# Problem: Minimum Absolute Difference
# Link: https://leetcode.com/problems/minimum-absolute-difference/
#
# Approach:
# First sort the array so that the minimum absolute difference must occur
# between adjacent elements.
#
# Iterate through the sorted array and compute the difference between every
# adjacent pair.
#
# If a smaller difference than the current minimum is found, update the
# minimum and reset the result list with the new pair.
#
# If the difference equals the current minimum, append the pair to the result.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space (excluding output list)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]: # type: ignore
        arr.sort()
        pair_list = []
        min_value = float("inf")

        for i in range(len(arr)-1):
            min_abs_diff = arr[i+1] - arr[i]

            if min_abs_diff < min_value:
                min_value = min_abs_diff
                pair_list = [[arr[i],arr[i+1]]]
            elif min_value == min_abs_diff:
                pair_list.append([arr[i],arr[i+1]])
        return pair_list