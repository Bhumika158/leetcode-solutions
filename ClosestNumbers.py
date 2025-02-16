"""Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    ##Time: O(n log n) , Space: O(n)
    sorted_arr= sorted(arr)
    min_val=float('inf')
    pairs=[]
    for i in range(1,len(sorted_arr)):
        diff = abs(sorted_arr[i] - sorted_arr[i - 1])
        if diff< min_val:
            min_val = diff
            pairs = [sorted_arr[i - 1], sorted_arr[i]]
        elif diff== min_val:
            pairs.extend([sorted_arr[i-1],sorted_arr[i]])
    return " ".join(map(str,pairs))

    ##CountingSort : Time: O(n), Space:O(n) >> Infeasible due to large memory requirements because as per question, it ranges from -10^7 to 10^7.
    # max_val = max(arr)
    # min_val = min(arr)
    # count = [0] * (max_val - min_val + 1)
    # for num in arr:
    #     count[num - min_val] += 1
    # sorted_arr = []
    # for i in range(len(count)):
    #     if count[i] > 0:
    #         sorted_arr.extend([i + min_val] * count[i])
    # min_diff = float('inf')
    # pairs = []
    #
    # for i in range(1, len(sorted_arr)):
    #     diff = sorted_arr[i] - sorted_arr[i - 1]
    #
    #     if diff < min_diff:
    #         min_diff = diff
    #         pairs = [[sorted_arr[i - 1], sorted_arr[i]]]
    #     elif diff == min_diff:
    #         pairs.append([sorted_arr[i - 1], sorted_arr[i]])
    #
    # return pairs

print(closestNumbers([5,2,3,4,1]))