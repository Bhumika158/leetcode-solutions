"""You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack."""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    ##Approach 1: Iterating over obstacles : Time: O(k), Space: O(k), Suitable when k(number of obstacles) is small and n(row/column is large)
    # left= c_q-1
    # right=n-c_q
    # up= n-r_q
    # down= r_q-1
    # up_left =min(up,left)
    # up_right=min(up,right)
    # down_left=min(down,left)
    # down_right=min(down,right)
    #
    # for r,c in obstacles:
    #     if r==r_q:
    #         if c<c_q:
    #             left=min(left,c_q-c-1)
    #         elif c>c_q:
    #             right=min(right,c-c_q-1)
    #     elif c==c_q:
    #         if r < r_q:
    #             down = min(down, r_q - r - 1)
    #         elif r > r_q:
    #             up = min(up, r - r_q - 1)
    #     elif abs(r - r_q) == abs(c - c_q):
    #         if r > r_q and c < c_q:
    #             up_left = min(up_left, r - r_q - 1)
    #         elif r > r_q and c > c_q:
    #             up_right = min(up_right, r - r_q - 1)
    #         elif r < r_q and c < c_q:
    #             down_left = min(down_left, r_q - r - 1)
    #         elif r < r_q and c > c_q:
    #             down_right = min(down_right, r_q - r - 1)
    # total_attackable = left + right + up + down + up_left + up_right + down_left + down_right
    # return total_attackable

    ##Approach 2: Using Set: Time: O(k+n), Space: O(k), Suitable when k(number of obstacles) is large and n(row/column is small)
    obstacles_set={(r,c) for r,c in obstacles}
    directions=[
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)  # down-right
    ]
    total_attackable = 0

    for dr,dc in directions:
        r,c= r_q+dr, c_q+dc
        while 1<=r<=n and 1<=c<=n:
            if (r,c) in obstacles_set:
                break
            total_attackable+=1
            r+=dr
            c+=dc
    return total_attackable

print(queensAttack(4,0,4,4,[]))