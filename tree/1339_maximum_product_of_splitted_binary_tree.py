# LeetCode 1339: Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
#
# Approach:
# The problem can be reduced to finding the best place to cut one edge in the tree.
# Cutting an edge splits the tree into two subtrees, and the product of their sums
# should be maximized.
#
# First, compute the total sum of all nodes in the tree using DFS.
# Then, perform another DFS (postorder traversal) to compute the sum of each subtree.
#
# For every subtree with sum S, consider it as one part of the split:
#   product = S * (total_sum - S)
# Track the maximum such product while traversing.
#
# Postorder traversal is required so that left and right subtree sums are known
# before computing the current node's subtree sum.
#
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (recursion stack)
