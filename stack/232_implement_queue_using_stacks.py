# LeetCode 232: Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Approach:
# Use two stacks to simulate queue behavior using only stack operations.
# One stack (in_stack) is used for push operations.
# Another stack (out_stack) is used for pop and peek operations.
#
# When popping or peeking, if out_stack is empty, move all elements from
# in_stack to out_stack. This reverses the order so that the oldest element
# comes to the top of out_stack, preserving FIFO behavior.
#
# Each element is moved at most once between stacks, giving amortized O(1)
# time per operation.
#
# Time Complexity: O(1) amortized per operation
# Space Complexity: O(n)
