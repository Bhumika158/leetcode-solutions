"""Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board A of size H*W with H rows and W columns. The board is divided into cells of size 1*1 with each cell indicated by its coordinate (1,j). The cell (i,j) has an integer Aij written on it. To create the toy Mason stacks Aij number of cubes of size 1*1*1 on the cell (i,j).

Given the description of the board showing the values of Aij and that the price of the toy is equal to the 3d surface area find the price of the toy."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    ##Time: O(H*W),Space: O(1)
    n_rows=len(A)
    n_cols= len(A[0])
    total = (n_rows*n_cols)*2
    for i in range(n_rows):
        for j in range(n_cols):
            val = A[i][j]

            # Add vertical faces exposed
            top_neighbor = A[i - 1][j] if i > 0 else 0
            left_neighbor = A[i][j - 1] if j > 0 else 0

            total += abs(val - top_neighbor)
            total += abs(val - left_neighbor)

            if j == n_cols - 1:
                total += val

            if i == n_rows - 1:
                total += val
    return total


print(surfaceArea([[1,3,4],[2,2,3],[1,2,4]]))