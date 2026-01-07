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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int: # type: ignore
        total_sum = 0
        max_product = 0
        MOD = 10**9 + 7
        def compute_total(node):
            if not node:
                return 0
            return node.val + compute_total(node.left)+compute_total(node.right)
        
        total_sum = compute_total(root)
        def dfs(node):
            nonlocal max_product
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            subtree_sum = node.val+ left_sum + right_sum

            product = subtree_sum * (total_sum - subtree_sum)

            max_product = max(max_product, product)
            return subtree_sum
        
        dfs(root)
        return max_product % MOD