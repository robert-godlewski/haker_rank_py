# Arrays in Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'maxMin' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
# My Solution solved in 20 min but incorrect, I don't really understand what they want.
def maxMin(k, arr):
    minNums =[]
    i = 0
    while i < k:
        num = min(arr)
        arr.remove(num)
        minNums.append(num)
        i += 1
    return max(minNums) - min(minNums)

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    unfairness = maxMin(2, [1,4,7,2])
