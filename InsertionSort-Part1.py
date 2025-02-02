"""Complete the insertionSort1 function in the editor below.

insertionSort1 has the following parameter(s):

n: an integer, the size of arr
arr: an array of integers to sort"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    v = arr[-1]
    i=n-2
    while i >= 0 and arr[i] > v:
        arr[i + 1] = arr[i]
        print(' '.join(map(str, arr)))
        i -= 1
    arr[i + 1] = v
    print(' '.join(map(str, arr)))

print(insertionSort1(14,[1,3,5,9,13,22,27,35,46,51,55,83,87,23]))