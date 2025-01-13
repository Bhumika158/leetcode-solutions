"""It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    ##Time: O(n), Space: O(1)
    bribes=0
    for i in range(len(q)):
        if q[i]-(i+1)>2:
            print("Too chaotic")
            return
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                bribes+=1
    print(bribes)

print(minimumBribes([2, 1, 5, 3, 4]))