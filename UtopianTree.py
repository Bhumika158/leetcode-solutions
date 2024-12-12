"""The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    ##Time: O(n), Space: O(1)

    # height=0
    # for i in range(n+1):
    #     if i%2==0:
    #         height+=1
    #     else:
    #         height*=2
    # return height

    ##Time: O(1), Space: O(1)
    if n%2==0:
        return (1<<(n//2+1))-1
    else:
        return (1<< ((n//2)+1))*2-2



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = 1

    for t_itr in range(t):
        n = 1

        result = utopianTree(n)

        print(result)