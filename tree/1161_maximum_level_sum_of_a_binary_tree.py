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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:      # type: ignore
        level = 1
        max_sum = float('-inf')
        queue = deque([root])
        best_level = 1

        if not root:
            return 
        
        while queue:
            size = len(queue)
            level_sum = 0
            for i in range(size): 
                current_node = queue.popleft()

                level_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            if level_sum > max_sum:
                max_sum = max(max_sum,level_sum)
                best_level = level
            level +=1

        return best_level


        