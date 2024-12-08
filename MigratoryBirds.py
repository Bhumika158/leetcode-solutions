"""Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids."""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    my_dic = {}
    for num in arr:
        if num in my_dic:
            my_dic[num] += 1
        else:
            my_dic[num] = 1
        max_freq = max(my_dic.values())

    return min([num for num, freq in my_dic.items() if freq == max_freq])


print(migratoryBirds([1,1,2,3,4]))