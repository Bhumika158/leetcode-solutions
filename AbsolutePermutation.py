"""We define P to be a permutation of the first n natural numbers in the range [1,n]. Let pos[i] denote the value at position i in permutation P using 1-based indexing.

P is considered to be an absolute permutation if |pos[i]-i|==k holds true for every i in range(1,n).

Given n and k, print the lexicographically smallest absolute permutation P. If no absolute permutation exists, print -1."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    ##Approach1: Time: O(n^2), Space: O(n)
    # res=[]
    # for i in range(1,n+1):
    #     if i - k > 0 and (i - k) not in res:
    #         res.append(i - k)
    #     elif i + k <= n and (i + k) not in res:
    #         res.append(i + k)
    #     else:
    #         return [-1]
    # return res

    ##Optimized Solution: Time: O(n), Space: O(n)
    if k==0:
        return list(range(1,n+1))

    if n%(2*k)!=0:
        return [-1]

    res=[]
    add=True
    for i in range(1,n+1):
        if add:
            res.append(i+k)
        else:
            res.append(i-k)

        if i%k==0:
            add=not add
    return res


print(absolutePermutation(10,3))