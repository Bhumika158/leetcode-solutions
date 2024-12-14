"""A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    ##Time: O(1), Space: O(1)
    remaining_choc= m%n
    last_prisoner = s+remaining_choc-1

    if last_prisoner>n:
        last_prisoner-=n
    return last_prisoner

    ##Approach 2: Better as it avoids overflowing with large inputs: Time: O(1), Space: O(1)
    # last_candy_position = (s - 1 + m - 1) % n + 1
    # return last_candy_position


print(saveThePrisoner(352926151,380324688,94730870))