# Arrays Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'dynamicArray' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
# My Solution - Solved in 30 min - Need to practice, had a hard time understanding at first
def dynamicArray(n, queries):
    print("queries:")
    print(queries)
    # better way than arr = [[]] * n because this way actually works
    arr = [[] for j in range(n)]
    last = 0
    # answer
    res = []
    print(arr)
    for q in queries:
        print(f"q = {q}")
        typeq = q[0]
        x = q[1]
        y = q[2]
        idx = ((x ^ last) % n)
        print(idx)
        if typeq == 1:
            arr[idx].append(y)
        elif q[0] == 2:
            last = arr[idx][y%len(arr[idx])]
            res.append(last)
        print(arr)
        print(res)
    return res

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    '''
    queries = [
        [1,0,5],
        [1,1,7],
        [1,0,3],
        [2,1,0],
        [2,1,1]
    ]
    result = dynamicArray(2, queries)
    print("Results:")
    print(result)
