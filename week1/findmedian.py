# Mock Test 1, ran out of time to figure out Test 2
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'findMedian' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# My solution - Solved in over 20 min!! (almost 30 min)
def mergeSort(arr):
    # Use to recurse through an array
    print(f"arr in = {arr}")
    if len(arr) > 1:
        # Splitting recursively
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        # Sorting
        i = 0
        j = 0
        k = 0
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        # adding the rest of left to the array
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        # adding the rest of right to the array
        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1
    print(f"arr out = {arr}")
    return arr


def findMedian(arr):
    # base case
    if len(arr) == 1: return arr[0]
    # Sorting
    arr = mergeSort(arr)
    # Grabbing the middle index of the array
    midInx = len(arr)//2
    return arr[midInx]

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    # Testing
    arr = [5,3,1,2,4]
    med = findMedian(arr)
    print(f"answer = {med}")
