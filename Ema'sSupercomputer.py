"""Ema built a quantum computer! Help her test its capabilities by solving the problem below.

Given a grid of size n*m, each cell in the grid is either good or bad.

A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.

Find the two largest valid pluses that can be drawn on good cells in the grid, and return an integer denoting the maximum product of their areas.
Note: The two pluses cannot overlap, and the product of their areas should be maximal."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    ##Time: O((N⋅M)^2 * min(N,M)), Space: O((N⋅M)*min(N,M))
    def get_max_plus_size(r, c):
        size = 0
        while True:
            for i in range(-size, size + 1):
                if grid[r + i][c] != 'G' or grid[r][c + i] != 'G':
                    return size - 1
            size += 1
            if r - size < 0 or r + size >= len(grid) or c - size < 0 or c + size >= len(grid[0]):
                return size - 1

    def get_area(size):
        return size * 4 + 1

    n, m = len(grid), len(grid[0])
    pluses = []

    # Find all valid pluses
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'G':
                size = get_max_plus_size(r, c)
                print(r,c,size)
                for s in range(size + 1):
                    pluses.append((get_area(s), r, c, s))
                    # print(pluses)

    # Sort by area in descending order
    pluses.sort(reverse=True, key=lambda x: x[0])
    print(pluses)

    # Check if two pluses overlap
    def overlap(p1, p2):
        area1, r1, c1, s1 = p1
        area2, r2, c2, s2 = p2
        cells1 = set()
        cells2 = set()

        for i in range(-s1, s1 + 1):
            cells1.add((r1 + i, c1))
            cells1.add((r1, c1 + i))
        for i in range(-s2, s2 + 1):
            cells2.add((r2 + i, c2))
            cells2.add((r2, c2 + i))

        return len(cells1 & cells2) > 0

    # Calculate max product
    max_product = 0
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            if not overlap(pluses[i], pluses[j]):
                max_product = max(max_product, pluses[i][0] * pluses[j][0])

    return max_product



print(twoPluses(["GGGGGG","GBBBGB","GGGGGG","GGBBGB","GGGGGG"]))