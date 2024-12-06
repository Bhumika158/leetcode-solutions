#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    ##Time: O(n), Space: O(1)
    h_s,l_s=scores[0],scores[0]
    max_cnt,min_cnt=0,0
    for score in scores:
        if score>h_s:
            h_s=score
            max_cnt+=1
        elif score<l_s:
            l_s= score
            min_cnt+=1
    return [max_cnt,min_cnt]





print(breakingRecords([10,5,20,20,4,5,2,25,1]))