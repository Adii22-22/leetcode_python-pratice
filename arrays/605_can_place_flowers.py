# LeetCode 605: Can Place Flowers
# Date solved: Dec 7, 2025
# Approach: Greedy Check (For-Loop)
# Explanation:
#   Iterate through each plot and check if a flower can be planted by ensuring:
#   - the current plot is empty,
#   - the left neighbor is empty or does not exist,
#   - the right neighbor is empty or does not exist.
#   If all conditions are satisfied, place a flower and reduce n.
#   This greedy strategy works because planting as early as possible
#   does not reduce future planting opportunities.
# Time Complexity: O(n)
# Space Complexity: O(1)
