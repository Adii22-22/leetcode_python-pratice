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
