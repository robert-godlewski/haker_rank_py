# Array Sort solution in Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'countingSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# My code - Correct here but incorrect in HakerRanker
def countingSort(arr):
    print(f"Array in = {arr}")
    # Find the Max number
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    # Initializing the length of count
    count = [0] * max_num
    print(f"count start = {count}")
    # Storing count for each elements count in the array
    i = 0
    while i < len(arr):
        #print(arr[i])
        count[arr[i]-1] += 1
        i += 1
    print(f"count (pre indexing)= {count}")
    # putting arr sorted in nums
    nums = []
    i = 0
    while i < len(count):
        if count[i] > 0:
            nums.append(i+1)
            count[i] -= 1
        else:
            i += 1
    print(f"solution = {nums}")
    arr = nums[:]
    return arr

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    '''
    arr1 = [1,1,3,2,1]
    arr1 = countingSort(arr1)
    print(f"Array after sorting = {arr1}")
