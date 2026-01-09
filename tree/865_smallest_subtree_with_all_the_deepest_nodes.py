# LeetCode 865: Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
#
# Approach:
# Use Depth First Search (DFS) to compute information bottom-up.
# For each node, DFS returns two values:
# 1) The maximum depth reachable from this node.
# 2) The subtree node that contains all deepest nodes below it.
#
# At each node:
# - Recursively compute depth and candidate node from left and right subtrees.
# - If one subtree is deeper, propagate that subtree's result upward.
# - If both subtrees have the same depth, the current node is the smallest
#   subtree that contains all deepest nodes (acts like LCA of deepest nodes).
#
# No global variables are needed since the correct answer naturally bubbles
# up through return values during DFS.
#
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (recursion stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore

        def dfs(node):
            if not node:
                return (0,None)

            (left_dept,left_node) = dfs(node.left)
            (right_dept,right_node) = dfs(node.right)

            if left_dept > right_dept:
                return (left_dept+1,left_node)
            elif right_dept > left_dept:
                return (right_dept+1,right_node)
            else:
                return (left_dept+1,node)

        return dfs(root)[1]