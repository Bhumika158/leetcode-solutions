"""Given an array of strings of digits, try to find the occurrence of a given pattern of digits. In the grid and pattern arrays, each string represents a row in the grid.The return value should be YES or NO, depending on whether the pattern is found. In this case, return YES."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    ##Approach 1: Time: O(rows_g * cols_g * rows_p * cols_p), Space: O(rows_g * cols_g + rows_p * cols_p)
    rows_g = len(G)
    cols_g = len(G[0])
    rows_p = len(P)
    cols_p = len(P[0])

    for i in range(rows_g-rows_p+1):
        for j in range(cols_g-cols_p+1):
            if all(G[i+k][j : j+cols_p]==P[k] for k in range(rows_p)):
                return "YES"
    return "NO"

    ##Approach 2: Time: O(rows_g * cols_g * rows_p * cols_p), Space: O(rows_g * cols_g + rows_p * cols_p + cols_g)
    # rows_g, cols_g = len(G), len(G[0])
    # rows_p, cols_p = len(P), len(P[0])
    #
    #
    # for i in range(rows_g - rows_p + 1):
    #     start_indices = [j for j in range(cols_g - cols_p + 1) if G[i][j:j + cols_p] == P[0]]
    #     for start_index in start_indices:
    #         if all(G[i + k][start_index:start_index + cols_p] == P[k] for k in range(1, rows_p)):
    #             return "YES"
    # return "NO"

print(gridSearch(["7283455864","6731158619","8988242643","3830589324","2229505813","5633845374","6473530293","7053106601","0834282956","4607924137"],["9505","3845","3530"]))