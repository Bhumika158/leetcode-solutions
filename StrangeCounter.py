"""There is a strange counter. At the first second, it displays the number 3. Each second, the number displayed by decrements by 1 until it reaches 1. In next second, the timer resets to 2*(initial number for prior cycle) and continues counting down. """

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):

    ##Time: O(logt), Space: O(1)
    # val,sum=3,3
    # if t<=val:
    #     return val-(t-1)
    # while val<t:
    #     p_v=val
    #     val*=2
    #     sum+=val
    #     if sum>=t:
    #         break
    # return val-(t-(sum-val+1))

    ##Refactored Approach: O(logt), Space: O(1)
    cycle_start = 3
    time = 1

    while t > time + cycle_start - 1:
        time += cycle_start
        cycle_start *= 2
    return cycle_start - (t - time)

print(strangeCounter(11))
