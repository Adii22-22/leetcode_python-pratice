# LeetCode 374: Guess Number Higher or Lower
# Date solved: Dec 1, 2025
# Approach: Binary Search
# Explanation:
#   Apply binary search between 1 and n. For each mid value, use the guess API:
#   if guess(mid) returns 0, we've found the number. If the API says our guess
#   is higher or lower, adjust the search space accordingly.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left+right)//2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid +1