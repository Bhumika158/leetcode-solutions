"""Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

Swap two elements.
Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task. Output is as follows.

If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

If elements can only be swapped, d[l] and d[r], output swap l r in the second line. l and r are the indices of the elements to be swapped, assuming that the array is indexed from 1 to n.
If elements can only be reversed, for the segment d[l...r], output reverse l r in the second line. l and r are the indices of the first and last elements of the subarray to be reversed, assuming that the array is indexed from 1 to n. Here d[l...r] represents the subarray that begins at index l and ends at index r, both inclusive.
If an array can be sorted both ways, by using either swap or reverse, choose swap.

If the array cannot be sorted either way, output no on the first line."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sorted_matches_original(a,s_a):
    return a==s_a
def almostSorted(arr):
    ##Time: O(n log n), Space: O(n)
    sorted_arr= sorted(arr)
    if sorted_matches_original(arr,sorted_arr):
        print("yes")
        return
    else:
        misplaced_index=[i for i in range(len(arr)) if arr[i]!=sorted_arr[i]]
        if len(misplaced_index)==2:
            l,r= misplaced_index[0],misplaced_index[1]
            arr[l],arr[r]=arr[r],arr[l]
            if sorted_matches_original(arr,sorted_arr):
                print("yes")
                print(f"swap {l+1} {r+1}")
            else:
                print("No")
            return
        if len(misplaced_index)>2:
            l, r = misplaced_index[0], misplaced_index[-1]
            sub_arr= arr[l:r+1]
            arr[l:r + 1] = sub_arr[::-1]
            if sorted_matches_original(arr,sorted_arr):
                print("yes")
                print(f"reverse {l+1} {r+1}")
            else:
                print("no")
            return
        print("no")

print(almostSorted([2,3,5,4]))