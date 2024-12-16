"""A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds,c  and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud,c[i]=1 , its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.

Given the values of ,n ,k and the configuration of the clouds as an array , determine the final value of  after the game ends."""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    ##Time: O(n), Space: O(1)
    n=len(c)
    e=100
    i=0
    while True:
        i=(i+k)%n
        e-=1
        if c[i]==1:
            e-=2
        if i==0:
            break
    return e

print(jumpingOnClouds([1,1,1,0,1,1,0,0,0,0],3))