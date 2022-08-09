# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'matchingStrings' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
# My code - Solved in 10 min
# O(n**2) time solution
def matchingStrings(strings, queries):
    ans = []
    for q in queries:
        temp = 0
        for s in strings:
            if s == q:
                temp += 1
        ans.append(temp)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    strings_count = int(input().strip())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(strings, queries)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
