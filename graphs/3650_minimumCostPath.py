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
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int: # type: ignore
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,2*w))
        dist = [float("inf")] * n
        dist[0] = 0
        heap = [(0,0)]
        visited = [False] * n

        while heap:
            d,u = heapq.heappop(heap) # type: ignore
            if u == n-1: return d
            if visited[u]: continue
            visited[u] = True

            for v,weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap,(dist[v], v)) # type: ignore
        return -1        