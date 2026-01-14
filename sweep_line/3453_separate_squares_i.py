# LeetCode 3453: Separate Squares I
# https://leetcode.com/problems/separate-squares-i/
#
# Approach:
# This solution uses a sweep line technique along the y-axis combined with a
# segment tree over compressed x-coordinates.
#
# Each square generates two events:
# - entering the square at y
# - leaving the square at y + side length
#
# While sweeping from bottom to top, the segment tree maintains the total
# covered width on the x-axis at the current y-interval. For each vertical
# slab between consecutive y-events, the covered width multiplied by the
# slab height contributes to the total area.
#
# All such slabs are recorded, allowing us to compute the total area first.
# Then, we iterate through the slabs again to find the minimum y-coordinate
# where the accumulated area reaches half of the total area.
#
# Overlapping squares are handled naturally because coverage is counted
# independently via the segment tree.
#
# This is an advanced geometry solution using sweep line + segment tree and
# is not expected to be derived during an interview without prior exposure.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
