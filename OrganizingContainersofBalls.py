"""David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    ##Time: O(nlogn), Space: O(n+m), where n=number of balls, m=number of containers.
    type_counts = [sum(row[i] for row in container) for i in range(len(container[0]))]
    container_sizes = [sum(row) for row in container]
    type_counts.sort()
    container_sizes.sort()
    if type_counts == container_sizes:
        return "Possible"
    else:
        return "Impossible"
print(organizingContainers([[0,2,1],[1,1,1],[2,0,0]]))