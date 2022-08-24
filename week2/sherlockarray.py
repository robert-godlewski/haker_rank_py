# Arrays Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'balancedSums' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
# My Solution - This doesn't really make sence at first
def balancedSums(arr):
    print(f"arr in = {arr}")
    if len(arr) < 4:
        print("Too Small to determine")
        return 'NO'
    a = arr[0]
    b = arr[1]
    c = arr[3]
    print(f"c = {c}")
    print(f"a + b = {a} + {b} = {a+b}")
    if a+b != c:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # Number of Cases to look at
    T = int(input().strip())
    # creating the cases
    for T_itr in range(T):
        # n = length of array
        n = int(input().strip())
        # building arrays off of n
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        #fptr.write(result + '\n')
        print(result)
    #fptr.close()
