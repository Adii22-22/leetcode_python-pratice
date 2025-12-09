# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number
# Date solved: Dec 9, 2025
# Approach: Sorting + Hash Map
# Explanation:
#   Sort the array to determine how many numbers are smaller than each value.
#   For each unique number, store the first index where it appears in the sorted list.
#   This index represents the count of smaller numbers.
#   Build the result by mapping each number in the original array to its stored count.
# Time Complexity: O(n log n)  # sorting dominates
# Space Complexity: O(n)       # dictionary + result list
