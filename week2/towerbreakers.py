# Math for Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'towerBreakers' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - Number of Towers
#  2. INTEGER m - Height of each tower
# My Solution - Took about an hour but needed help
def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()
    '''
    winner = towerBreakers(2, 6)
    print(f"The winner is player {winner}")
