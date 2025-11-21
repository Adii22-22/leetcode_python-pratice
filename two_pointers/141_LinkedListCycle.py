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
#----------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
