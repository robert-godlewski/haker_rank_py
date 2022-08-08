# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
# My Code - Solved under 10 minutes
def plusMinus(arr):
    total = len(arr)
    posList = []
    negList = []
    z = 0
    for i in arr:
        if i < 0: negList.append(i)
        elif i > 0: posList.append(i)
        else: z += 1
    pos = len(posList)
    neg = len(negList)
    posRatio = pos/total
    negRatio = neg/total
    zRatio = z/total
    print(posRatio)
    print(negRatio)
    print(zRatio)
    

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
