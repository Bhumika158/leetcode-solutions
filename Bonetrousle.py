"""Once upon a time, Papyrus the skeleton went to buy some pasta from the store. The store's inventory is bare-bones and they only sell one thing — boxes of uncooked spaghetti! The store always stocks exactly k boxes of pasta, and each box is numbered sequentially from 1 to k. This box number also corresponds to the number of sticks of spaghetti in the box, meaning the first box contains 1 stick, the second box contains 2 sticks, the third box contains 3 sticks, …, and the kth box contains k sticks. Because they only stock one box of each kind, the store has a tendon-cy to sell out of spaghetti.

During each trip to the store, Papyrus likes to buy exactly n sticks of spaghetti by purchasing exactly b boxes (no more, no less). Not sure which boxes to purchase, Papyrus calls Sherlock Bones for help but he's also stumped! Do you have the guts to solve this puzzle?

Given the values of n,k and b for t trips to the store, determine which boxes Papyrus must purchase during each trip. For each trip, print a single line of  distinct space-separated integers denoting the box number for each box of spaghetti Papyrus purchases (recall that the store only has one box of each kind). If it's not possible to buy  sticks of spaghetti by purchasing  boxes, print -1 instead."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonetrousle' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER k
#  3. INTEGER b
#

def bonetrousle(n, k, b):
    ##Time: O(b), Space:O(b)
    min_sum = b * (b + 1) // 2
    max_sum = sum(range(k - b + 1, k + 1))
    if n < min_sum or n > max_sum:
        return [-1]
    result = list(range(1, b + 1))
    print(result)
    current_sum = min_sum
    for i in range(b - 1, -1, -1):
        max_val = k - (b - 1 - i)
        diff = n - current_sum
        increase = min(diff, max_val - result[i])
        result[i] += increase
        current_sum += increase
        if current_sum == n:
            break
    return result


print(bonetrousle(12,8,3))