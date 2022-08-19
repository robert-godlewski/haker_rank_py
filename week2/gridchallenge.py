# Strings and arrays Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'gridChallenge' function below.
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
# My Solution - 30 min - Still incorrect in HackerRank
def checkgroup(arr):
    prev = arr[0]
    for letter in arr:
        if letter == arr[0]:
            pass
        elif ord(letter) > ord(prev):
            return 'NO'
        prev = letter
    return 'YES'

def gridChallenge(grid):
    in_order = 'NO'
    i = 0
    while i < len(grid):
        arr = list(grid[i])
        grid[i] = arr
        i += 1
    i = 0
    temp = []
    while i < len(grid):
        j = 0
        while j < len(grid):
            temp.append(grid[j][i])
            j += 1
        in_order = checkgroup(temp)
        if in_order == 'NO':
            return in_order
        temp = []
        i += 1
    return 'YES'

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        fptr.write(result + '\n')
    fptr.close()
    '''
    grid = ['abc','ade','efg']
    print(f"grid at start = {grid}")
    confirm = gridChallenge(grid)
    print(f"Is in alphabetical order? {confirm}")
