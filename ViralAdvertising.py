"""HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those  people (i.e.,5//2 ) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day, (5//2)*3 people receive the advertisement.

Each day, n//2 of the recipients like the advertisement and will share it with  friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1."""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    ##Time: O(n), Space: O(1)
    S = 5
    C =0
    for i in range(1,n+1):
        L = S // 2
        C += L
        S=L*3
    return C

print(viralAdvertising(5))