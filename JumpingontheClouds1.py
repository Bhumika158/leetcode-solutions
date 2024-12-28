"""There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    ##Time: O(n), Space: O(1)
    i,j=0,0
    while i<len(c)-1:
        if (i+2)<len(c) and c[i+2]==0:
            j+=1
            i+=2
        else:
            i+=1
            j+=1
    return j

print(jumpingOnClouds([0,0,0,0,1,0]))