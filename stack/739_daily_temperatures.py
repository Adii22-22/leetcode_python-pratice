# LeetCode 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
#
# Approach:
# Use a monotonic decreasing stack that stores indices of days.
# Traverse the temperature list from left to right.
# For each day, while the current temperature is greater than the
# temperature at the index on top of the stack, pop that index and
# calculate the number of days waited.
# Push the current index onto the stack.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # type: ignore
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
        return result