"""Little Bobby loves chocolate. He frequently goes to his favorite  store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    n_choc=t_wrapper= n//c
    while t_wrapper>=m:
        traded= t_wrapper//m
        n_choc+=traded
        t_wrapper=traded+ (t_wrapper%m)
    return n_choc

print(chocolateFeast(15,3,2))