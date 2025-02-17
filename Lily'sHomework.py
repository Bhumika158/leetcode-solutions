"""Consider an array of n distinct integers,arr = [a[0],a[1]...a[n-1]] . George can swap any two elements of the array any number of times. An array is beautiful if the sum of |arr[i]-arr[i-1| among o<i<n is minimal.

Given the array arr, determine and return the minimum number of swaps that should be performed in order to make the array beautiful."""

#!/bin/python3

import math
import os
import random
import re
import sys
from array import array
from itertools import cycle


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    arr_sorted = sorted(arr)
    return min(min_swaps(arr,arr_sorted),min_swaps(arr,arr_sorted[::-1]))

def min_swaps(arr,targeted_arr):
    n=len(arr)
    index_map = {val:idx for idx,val in enumerate(arr)}
    print(index_map)
    visited = [False]*n
    print(visited)
    swaps=0
    for i in range(n):
        if visited[i] or arr[i]==targeted_arr[i]:
            continue
        cycle_size=0
        x=i
        while not visited[x]:
            visited[x] = True
            cycle_size+=1
            x= index_map[targeted_arr[x]]
        if cycle_size>1:
            swaps += (cycle_size-1)
    return swaps

print(lilysHomework([7,15,12,3]))