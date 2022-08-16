# Arrays solved in Aug 2022
# #!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'sockMerchant' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
# My solution - Took about 20 min
def sockMerchant(n, ar):
    # Finding a maximum
    max = ar[0]
    for i in ar:
        if i > max: 
            max = i
    # Setting up the number of counts per number
    counts = [0] * max
    i = 0
    while i < n:
        counts[ar[i]-1] += 1
        i += 1
    # Calculating the amount of pairs per number
    pairs = 0
    for count in counts:
        temp = count//2
        pairs += temp
    return pairs

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    arr = [1,2,1,2,1,3,2]
    pairs = sockMerchant(7, arr)
    print(f"The answer = {pairs}")
