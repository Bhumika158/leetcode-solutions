"""You are given a 2D matrix of dimension m*n and a positive integer r. You have to rotate the matrix r times and print the resultant matrix. Rotation should be in anti-clockwise direction.

Note that in one rotation, you have to shift elements by one step only.It is guaranteed that the minimum of m and n will be even."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    ##Time: O(m*n), Space: O(ring size)
    #Find number of layers:
    m,n=len(matrix),len(matrix[0])
    layers= min(m,n)//2
    print(layers)

    # Extract each layer, rotate it, and place it back
    for layer in range(layers):
        # Extract the ring for this layer
        top = layer
        bottom = m - layer - 1
        left = layer
        right = n - layer - 1

        ring = []
        #Top Row
        for col in range(left, right + 1):
            ring.append(matrix[top][col])
        #Right Column
        for row in range(top + 1, bottom + 1):
            ring.append(matrix[row][right])
        #Bottom Row
        for col in range(right-1,left-1,-1):
            ring.append(matrix[bottom][col])
        # Left Column
        for row in range(bottom-1, top,-1):
            ring.append(matrix[row][left])

        #Rotate the ring
        ring_length = len(ring)
        r_effective = r % ring_length
        rotated_ring = ring[r_effective:] + ring[:r_effective]

        # Place the rotated ring back into the matrix
        index = 0
        # Top row
        for col in range(left, right + 1):
            matrix[top][col] = rotated_ring[index]
            index += 1
        # Right column
        for row in range(top + 1, bottom + 1):
            matrix[row][right] = rotated_ring[index]
            index += 1
        # Bottom row
        for col in range(right - 1, left - 1, -1):
            matrix[bottom][col] = rotated_ring[index]
            index += 1

        # Left column
        for row in range(bottom - 1, top, -1):
            matrix[row][left] = rotated_ring[index]
            index += 1

    # Print the rotated matrix
    for row in matrix:
        print(" ".join(map(str, row)))
print(matrixRotation([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],2))