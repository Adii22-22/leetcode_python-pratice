# LeetCode 875: Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
#
# Approach:
# Use binary search on the answer (eating speed). The search space ranges from
# 1 to the maximum pile size. For a given speed, calculate total hours required
# by summing ceil(pile / speed) for all piles. If total hours are within the
# given limit, try a smaller speed; otherwise, increase the speed.
#
# Time Complexity: O(n log M), where n is the number of piles and M is the maximum pile size
# Space Complexity: O(1)
