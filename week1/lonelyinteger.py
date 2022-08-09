# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# My code - Solved in 20 min
# Best = O(1)
# Worst = O(n**2)
def lonelyinteger(a):
    #print(f"array in = {a}")
    if len(a) <= 1:
        #print(f"answer = {a[0]}")
        return a[0]
    i = 0
    is_found = False
    num = 0
    while i < len(a) and not is_found:
        j = 0
        while j < len(a):
            if j == i:
                print("skip")
                pass
            else:
                #print(f"i = {i}, j = {j}")
                #print(f"Comparing a[i] = {a[i]} and a[j] = {a[j]}")
                if a[j] == a[i]:
                    is_found = False
                    #print("Haven't found it yet")
                    break
                else:
                    is_found = True
                    num = i
            j += 1
        if is_found:
            #print(f"Final index is {num}")
            break
        else:
            i += 1
    #print(f"answer = {a[num]}")
    return a[num]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()
    '''
    # Testing code
    a1 = [1,2,3,4,3,2,1]
    single1 = lonelyinteger(a1)
    a2 = [1]
    single2 = lonelyinteger(a2)
    a3 = [1,1,2]
    single3 = lonelyinteger(a3)
    a4 = [0,0,1,2,1]
    single4 = lonelyinteger(a4)
    '''

