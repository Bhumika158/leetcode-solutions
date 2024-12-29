"""You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.

Find all the cavities on the map and replace their depths with the uppercase character X"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    grid = [list(row) for row in grid]
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            if grid[i][j] > grid[i - 1][j] and grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i][j - 1] and grid[i][
                j] > grid[i][j + 1]:
                grid[i][j] = 'X'
    return ["".join(row) for row in grid]
print(cavityMap(['1112', '1912', '1892', '1234']))