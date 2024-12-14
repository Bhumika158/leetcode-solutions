"""Given a sequence of n integers,p(1),p(2)..p(n)  where each element is distinct and satisfies 1<=p(x)<=n. For each x where 1<=x<=n, that x is  increments from 1 to n, find any integer y such that p(p(y))===x and keep a history of the values of y in a return array."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    ##Time: O(n^2), Space: O(n)
    # n=len(p)
    # res=[]
    # for i in range(1,n+1):
    #     res.append(p.index(p.index(i)+1)+1)
    # return res

    ##using dic : O(n), Space: O(n)
    my_dic= {value:i+1 for i,value in enumerate(p)}

    res= [my_dic[my_dic[i]] for i in range(1,len(p)+1)]
    return res


print(permutationEquation([5,2,1,3,4]))