"""Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6 digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and return the sorted array."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Time: O(NlogN⋅M), Space: O(N)
    # new_list= [int(i) for i in unsorted]
    # new_list.sort()
    # final_list= [str(i) for i in new_list]
    # return final_list

    # Using Sorted with key: Time: O(NlogN⋅M), Space: O(N):
    # return sorted(unsorted, key=lambda x: (len(x), x))

    # Using inbuilt sort , Time: O(NlogN.M) , SPace: O(1)
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted


print(bigSorting(['1','200','150','3']))
