# Arrays solved in Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'birthday' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
# My code - Solved in 20 min
def birthday(s, d, m):
    print(s)
    ans = 0
    i = len(s)-1
    while i >= m-1:
        subtotal = 0
        print(f"i = {i}")
        j = 0
        while j < m:
            print(f"j = {j}")
            print(f"s[i-j] = {s[i-j]}")
            subtotal += s[i-j]
            j += 1
        print(f"subtotal of {i} and {m} others = {subtotal}")
        if subtotal == d: ans += 1
        print(f"ans = {ans}")
        i -= 1
    print(f"Final answer = {ans}")
    return ans

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    result = birthday([2,2,1,3,2],4,2)
    print(result)
