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
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Build events and x-coordinates
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # start square
            events.append((y + l, -1, x, x + l)) # end square
            xs.add(x)
            xs.add(x + l)

        xs = sorted(xs)
        x_index = {v: i for i, v in enumerate(xs)}
        n = len(xs)

        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if count[node] > 0:
                length[node] = xs[r] - xs[l]
            elif l + 1 == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                count[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid, r, ql, qr, val)
            push_up(node, l, r)


        events.sort()

        total_area = 0.0
        prev_y = events[0][0]
        slabs = []  

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                width = length[1]
                if width > 0:
                    slabs.append((prev_y, y, width))
                    total_area += width * dy
            update(1, 0, n - 1, x_index[x1], x_index[x2], typ)
            prev_y = y

        half = total_area / 2.0
        acc = 0.0


        for y1, y2, width in slabs:
            area = width * (y2 - y1)
            if acc + area >= half:
                return y1 + (half - acc) / width
            acc += area

        return 0.0
