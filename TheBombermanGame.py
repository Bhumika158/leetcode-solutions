"""Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell i,j any valid cells [i+-1,j] and [i,j+-1] are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
After one second, Bomberman does nothing.
After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after N seconds."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    ##Time: O(R*C), Space: O(R*C)
    rows = len(grid)
    cols = len(grid[0])

    if n == 1:
        return grid
    elif n % 2 == 0:
        return ["O" * cols for _ in range(rows)]

    def detonate(grid):
        detonated_grid = [["O"] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O":
                    detonated_grid[i][j] = "."
                    if i > 0:
                        detonated_grid[i - 1][j] = "."
                    if i < rows - 1:
                        detonated_grid[i + 1][j] = "."
                    if j > 0:
                        detonated_grid[i][j - 1] = "."
                    if j < cols - 1:
                        detonated_grid[i][j + 1] = "."
        return detonated_grid

    state1 = detonate(grid)
    state2 = detonate(state1)
    if (n // 2) % 2 == 1:
        return ["".join(row) for row in state1]
    else:
        return ["".join(row) for row in state2]

print(bomberMan(6,[[".",".","."],[".","O","."],[".",".","."]]))