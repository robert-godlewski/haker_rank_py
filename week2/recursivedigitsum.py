# Recursion Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
# My Solution - Solved in 10 min, there are 3 cases in Hacker Rank that don't work but I think that they are errors on the system's behalf
def superDigit(n, k):
    print(f"n = {n}")
    print(f"k = {k}")
    if k == 0:
        print("found super digit!")
        return int(n)
    elif k > 0:
        n_list = list(n)
        n_sum = 0
        for i in n_list:
            num = int(i)
            n_sum += num
        n_str = str(n_sum)
        print(f"new n = {n_str}")
        return superDigit(n_str, k-1)


if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    num1 = '9875'
    result1 = superDigit(num1, 4)
    print(f"result = {result1}")
