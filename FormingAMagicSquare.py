"""We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

from itertools import permutations

def generate_magic_squares():
    magic_squares = []
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for perm in permutations(nums):
        square = [perm[:3], perm[3:6], perm[6:]]

        # Check rows, columns, and diagonals
        if (sum(square[0]) == 15 and
                sum(square[1]) == 15 and
                sum(square[2]) == 15 and
                sum([square[i][0] for i in range(3)]) == 15 and
                sum([square[i][1] for i in range(3)]) == 15 and
                sum([square[i][2] for i in range(3)]) == 15 and
                sum([square[i][i] for i in range(3)]) == 15 and
                sum([square[i][2 - i] for i in range(3)]) == 15):
            magic_squares.append(square)

    return magic_squares
def formingMagicSquare(s):
    ## Hardcoding Possible MagicSquares: Time: O(1), Space: O(1)
    # magic_squares = [
    #     [8, 1, 6, 3, 5, 7, 4, 9, 2],
    #     [6, 1, 8, 7, 5, 3, 2, 9, 4],
    #     [4, 9, 2, 3, 5, 7, 8, 1, 6],
    #     [2, 9, 4, 7, 5, 3, 6, 1, 8],
    #     [8, 3, 4, 1, 5, 9, 6, 7, 2],
    #     [4, 3, 8, 9, 5, 1, 2, 7, 6],
    #     [6, 7, 2, 1, 5, 9, 8, 3, 4],
    #     [2, 7, 6, 9, 5, 1, 4, 3, 8]
    # ]
    # flat_s = [num for row in s for num in row]
    # min_cost = float('inf')
    # for magic in magic_squares:
    #     cost = sum(abs(flat_s[i] - magic[i]) for i in range(9))
    #     min_cost = min(min_cost, cost)
    #
    # return min_cost

    ##Generating Magic Square: Time: O(n!), Space: O(1)
    magic_squares = generate_magic_squares()
    min_cost = float('inf')
    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        min_cost = min(min_cost, cost)

    return min_cost




print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))