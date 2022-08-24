# Strings and recursion Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'counterGame' function below.
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
# My Solution - Incorrect but not sure why
def counterGame(n, is_rich=False):
    print(f"n start = {n}")
    if n == 1 and is_rich:
        return 'Richard'
    elif n == 1:
        return 'Louise'
    if n % 2 != 0:
        diff = int(n//2)
        n -= diff
    else:
        n = int(n/2)
    is_rich = not is_rich
    return counterGame(n, is_rich)

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = counterGame(n)
        fptr.write(result + '\n')
    fptr.close()
    '''
    num1 = 1
    result1 = counterGame(num1)
    print(f"First result = {result1}")
    num2 = 6
    result2 = counterGame(num2)
    print(f"Second result = {result2}")
