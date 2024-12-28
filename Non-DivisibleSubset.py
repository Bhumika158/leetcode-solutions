"""Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1
    result = 0
    if remainder_count[0] > 0:
        result += 1
    for r in range(1, (k // 2) + 1):
        if r != k - r:
            result += max(remainder_count[r], remainder_count[k - r])
    if k % 2 == 0:
        result += 1 if remainder_count[k // 2] > 0 else 0

    return result

print(nonDivisibleSubset(7,[278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]))