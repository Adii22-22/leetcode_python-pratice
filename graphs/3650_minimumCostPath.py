# LeetCode 3650
# Problem: Minimum Cost Path
# Link: https://leetcode.com/problems/minimum-cost-path/
#
# Approach:
# Build a graph where each edge (u, v, w) is treated as:
# - u -> v with cost w
# - v -> u with cost 2*w
# This models the asymmetric cost condition given in the problem.
#
# Use Dijkstra’s algorithm starting from node 0 to find the minimum cost
# to reach node n-1.
#
# Maintain a distance array initialized with infinity and a min-heap
# to always process the node with the smallest known distance.
#
# Use a visited array to ensure each node is finalized only once.
# As soon as node n-1 is popped from the heap, return the current distance.
#
# If node n-1 is unreachable, return -1.
#
# Time Complexity: O((n + m) log n), where m is the number of edges
# Space Complexity: O(n + m)
