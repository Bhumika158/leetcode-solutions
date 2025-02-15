"""Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times."""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    if not arr:
        return []
    res = [0] * 100
    for i in arr:
        res[i] += 1
    return res

print(countingSort([63,54,17,78,43,70,32,97,16,94,74,18,60,61,35,83,13,56,75,52,70,12,24,37,17,0,16,64,34,81,82,24,69,2,30,61,83,37,97,16,70,53,0,61,12,17,97,67,33,30,49,70,11,40,67,94,84,60,35,58,19,81,16,14,68,46,42,81,75,87,13,84,33,34,14,96,7,59,17,98,79,47,71,75,8,27,73,66,64,12,29,35,80,78,80,6,5,24,49,82]))
