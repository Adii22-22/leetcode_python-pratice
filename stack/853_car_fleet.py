# LeetCode 853: Car Fleet
# https://leetcode.com/problems/car-fleet/
#
# Approach:
# Pair each car's position and speed together and sort the cars by position.
# Process the cars from the one closest to the target to the farthest.
#
# For each car, calculate the time it would take to reach the target if it were
# driving alone. Use a stack to keep track of arrival times of existing fleets.
#
# If the current car's arrival time is greater than the top of the stack, it
# cannot catch up to the fleet ahead and forms a new fleet (push to stack).
# If the arrival time is less than or equal to the top, it merges with the
# fleet ahead and does not create a new fleet.
#
# The number of car fleets is equal to the size of the stack at the end.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the stack
