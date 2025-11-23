# 1262. Greatest Sum Divisible by Three
# Difficulty: Medium
# Date Solved: Nov 23, 2025
#
# Approach:
# - Compute the total sum of the array.
# - If total % 3 == 0 → we can return total immediately.
# - Otherwise:
#     • Numbers with remainder 1 and remainder 2 (mod 3) are separated.
#     • We track the two smallest numbers in each category:
#         - smallest and second smallest with remainder 1
#         - smallest and second smallest with remainder 2
# - For remainder 1:
#     Option A: remove smallest remainder-1 number
#     Option B: remove two smallest remainder-2 numbers
#
# - For remainder 2:
#     Option A: remove smallest remainder-2 number
#     Option B: remove two smallest remainder-1 numbers
#
# - Return the maximum valid sum.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int: # type: ignore
        total = sum(nums)

        small1 = small2 = float('inf')
        large1 = large2 = float('inf')

        for num in nums:
            r = num % 3

            if r == 1:
                if num < small1:
                    small2 = small1
                    small1 = num
                elif num < small2:
                    small2 = num

            elif r == 2:
                if num < large1:
                    large2 = large1
                    large1 = num
                elif num < large2:
                    large2 = num

        remainder = total % 3

        if remainder == 0:
            return total

        elif remainder == 1:
            candidate = []
            if small1 != float('inf'):
                candidate.append(total - small1)
            if large2 != float('inf'):
                candidate.append(total - (large1 + large2))
            return max(candidate)

        else:  # remainder == 2
            candidate = []
            if large1 != float('inf'):
                candidate.append(total - large1)
            if small2 != float('inf'):
                candidate.append(total - (small1 + small2))
            return max(candidate)
