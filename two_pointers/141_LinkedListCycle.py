# 141. Linked List Cycle
# Difficulty: Easy
# Solved on: Nov 20, 2025
#
# Approach:
# - Uses Floyd’s Tortoise and Hare algorithm (two-pointer technique).
# - Slow pointer moves 1 step, fast pointer moves 2 steps.
# - If the linked list has a cycle, fast and slow will eventually meet.
# - If fast reaches None, the list has no cycle.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
