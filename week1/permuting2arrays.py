# Arrays solved in Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'twoArrays' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
# My code - for some reason this is wrong in Haker Ranker but not sure why?
def twoArrays(k, A, B):
    n = len(A)
    print(f"k = {k}")
    print(f"A = {A}")
    print(f"B = {B}")
    is_yes = False
    i = 0
    while i < n:
        print(f"i = {i}")
        compare = A[i] + B[i]
        print(f"compare = {compare}")
        if compare >= k: is_yes = True
        else:
            is_yes = False
            break
        i += 1
    if is_yes: return "YES"
    else: return "NO"


if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        fptr.write(result + '\n')
    fptr.close()
    '''
    a1 = [1,2,3]
    b1 = [9,8,7]
    ans1 = twoArrays(10,a1,b1)
    print(f"Answer = {ans1}")
    a2 = [1,2,2,1]
    b2 = [3,3,3,4]
    ans2 = twoArrays(5,a2,b2)
    print(f"Answer = {ans2}")
