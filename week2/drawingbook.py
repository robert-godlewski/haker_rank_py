# Math Algorithm Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'pageCount' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
# My solution - Solution took me about 30 min to solve
# Didn't quite understand at first
# Solution is O(1)
def pageCount(n, p):
    # Base cases
    '''
    if p == 0 or p == 1:
        return 0
    if n-1 == p and p%2 == 0:
        return 0
    elif n-1 == p:
        return 1
    '''
    # diff1 is the amount from the start
    diff1 = p//2
    # diff2 is the amount from the end
    diff2 = n//2-diff1
    # Returning the smaller of the 2
    if diff1 <= diff2:
        return diff1
    else:
        return diff2

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    p = int(input().strip())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    n = 5
    p = 3
    count = pageCount(n, p)
    print(f"answer = {count}")
