# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# My code - Soved in 30 min
def diagonalDifference(arr):
    print(f"arr in = {arr}")
    if len(arr) <= 1:
        return 0
    else:
        n = len(arr)
        print(f"length of the array = {n}")
        d1 = 0
        d2 = 0
        print(f"d1 start = {d1}")
        print(f"d2 start = {d2}")
        i = 0
        k = n-1
        while i < len(arr):
            print(f"i = {i}")
            print(f"k = {k}")
            print(f"adding {arr[i][i]} to d1")
            d1 += arr[i][i]
            print(f"d1 = {d1}")
            print(f"adding {arr[k][i]} to d2")
            d2 += arr[k][i]
            print(f"d2 = {d2}")
            i+=1
            k-=1
        if d1 >= d2:
            print(f"result = {d1-d2}")
            return d1-d2
        else:
            print(f"result = {d2-d1}")
            return d2-d1

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    # Testing
    arr1 = [
        [1,2,3],
        [4,5,6],
        [9,8,9]
    ]
    d1 = diagonalDifference(arr1)
    arr2 = [
        [11,2,4],
        [4,5,6],
        [10,8,-12]
    ]
    d2 = diagonalDifference(arr2)
