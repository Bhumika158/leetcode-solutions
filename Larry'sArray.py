"""Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. He must determine whether the array can be sorted using the following operation any number of times:

Choose any 3 consecutive indices and rotate their elements in such a way that ABC > BCA >CAB >ABC."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    ##Time: O(n^2), Space: O(1)
    n=len(A)
    inversion=0
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                inversion+=1
    if inversion%2==0:
        return "YES"
    else:
        return "NO"

    ## Merge Sort: Time: O(n log n), Space: O(n)
#     temp_arr = [0] * len(A)
#     inversions = merge_sort_and_count(A, temp_arr, 0, len(A) - 1)
#     return "YES" if inversions % 2 == 0 else "NO"
#
# def merge_sort_and_count(arr, temp_arr, left, right):
#     inversions = 0
#     if left < right:
#         mid = (left + right) // 2
#         inversions += merge_sort_and_count(arr, temp_arr, left, mid)
#         inversions += merge_sort_and_count(arr, temp_arr, mid + 1, right)
#         inversions += merge_and_count(arr, temp_arr, left, mid, right)
#     return inversions
# def merge_and_count(arr, temp_arr, left, mid, right):
#     i = left
#     j = mid + 1
#     k = left
#     inversions = 0
#     while i <= mid and j <= right:
#         if arr[i] <= arr[j]:
#             temp_arr[k] = arr[i]
#             i += 1
#         else:
#             temp_arr[k] = arr[j]
#             inversions += (mid - i + 1)
#             j += 1
#         k += 1
#     while i <= mid:
#         temp_arr[k] = arr[i]
#         i += 1
#         k += 1
#     while j <= right:
#         temp_arr[k] = arr[j]
#         j += 1
#         k += 1
#     for i in range(left, right + 1):
#         arr[i] = temp_arr[i]
#
#     return inversions
print(larrysArray([1,6,5,2,4,3]))