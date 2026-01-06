# LeetCode 1161: Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#
# Approach:
# Use Breadth-First Search (level-order traversal) with a queue to process
# the binary tree level by level.
#
# At the start of each level, take the current queue size to know how many
# nodes belong to that level. Process exactly those nodes to compute the
# sum of values for the current level.
#
# Track the maximum level sum seen so far and store the corresponding
# level number. Levels are counted starting from 1 (root level).
#
# After processing all levels, return the level index that has the maximum sum.
#
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), due to the queue used for BFS
