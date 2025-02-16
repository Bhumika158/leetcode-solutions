"""Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an insertion sort performs when sorting an array?"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    ##Time: O(n^2), Space: O(1)
    # n= len(arr)
    # count=0
    # for i in range(1, n):
    #     key = arr[i]
    #     j = i - 1
    #     print(key,j)
    #
    #     while j >= 0 and arr[j] > key:
    #         arr[j + 1] = arr[j]
    #         j -= 1
    #         count+=1
    #     arr[j + 1] = key
    #     # print(" ".join(map(str, arr)))
    # return count

    #Using Merge Sort: Time: O(nlog n), Space: O(n):
    temp_arr = arr[:]
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Left subarray index
    j = mid + 1 # Right subarray index
    k = left    # Merged subarray index
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Count shifts
            j += 1
        k += 1

    # Copy remaining elements of left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy sorted elements back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


print(insertionSort([2,1,3,1,2]))