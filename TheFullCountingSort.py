"""Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

Design your counting sort to be stable."""

#!/bin/python3

import math
import os
import random
import re
import sys
from typing import final

from numpy.ma.core import max_val


#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    n= len(arr)
    for i in range(n//2):
        arr[i][1]='-'
    max_value = max(int(pair[0]) for pair in arr)
    count= [[] for _ in range(max_value + 1)]
    for pair in arr:
        index= int(pair[0])
        count[index].append(pair[1])
    final_res= ""
    for i in count:
        for j in i:
            final_res += f"{j} "
    print(final_res)
print(countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]))