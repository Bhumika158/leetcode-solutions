"""There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist."""

# !/bin/python3

import math
from functools import reduce



# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

## Time: O(n log(k) + m log(k1) + root**0.5), Space: O(root**0.5)
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_list(arr):
    return reduce(lcm, arr)


def gcd_list(arr):
    return reduce(math.gcd, arr)


def find_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)
    divisors = find_divisors(gcd_b)
    count = sum(1 for d in divisors if d % lcm_a == 0)
    return count


print(getTotalX([2,4],[24,36]))