# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
# My Code - Solved in 20 min
def miniMaxSum(arr):
    low = arr[0]
    high = arr[0]
    subtotal = 0
    for num in arr:
        if num < low: low = num
        if num > high: high = num
        subtotal += num
    minSum = subtotal - high
    maxSum = subtotal - low
    print(f"{minSum} {maxSum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

