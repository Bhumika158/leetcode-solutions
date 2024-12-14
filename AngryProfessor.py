"""A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (ArrivalTime<=0) to arrived
late (ArrivalTime>0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    ##Time: O(n), Space: O(1)
    on_time_count= sum(1 for i in a if i<=0)

    return "YES" if on_time_count<k else "NO"

print(angryProfessor(3,[-1,-3,4,2]))