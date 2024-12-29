"""There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, presented as binary strings, determine the maximum number of topics a 2-person team can know. Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. Also determine the number of teams that know the maximum number of topics. Return an integer array with two elements. The first is the maximum number of topics known, and the second is the number of teams that know that number of topics."""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    ##Time: O(n^2*m), Space: O(1)
    l=len(topic)
    max_topics = 0
    team_count = 0
    for i in range(0,l):
        for j in range(i+1,l):
            topics_known = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if topics_known>max_topics:
                max_topics=topics_known
                team_count =1
            elif topics_known==max_topics:
                team_count+=1
    return [max_topics,team_count]

print(acmTeam(["10101","11110","00010"]))