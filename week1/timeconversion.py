# Array solved Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# My Code - Solved in 20 min
def timeConversion(s):
    print(s)
    sArr = s.split(":")
    print(sArr)
    is_12 = False
    if sArr[0] == '12': is_12 = True
    end = sArr.pop()
    print(end)
    print(sArr)
    endsp = list(end)
    print(endsp)
    is_evening = False
    endsp.pop()
    aOrP = endsp.pop()
    if aOrP == 'P': is_evening = True
    sec = endsp[0] + endsp[1]
    print(sec)
    sArr.append(sec)
    print(sArr)
    if is_evening and not is_12:
        hr = int(sArr[0])
        hr += 12
        sArr[0] = str(hr)
    elif is_12 and not is_evening:
        sArr[0] = '00'
    result = f"{sArr[0]}:{sArr[1]}:{sArr[2]}"
    print(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
    '''
    s = '07:05:45PM'
    result = timeConversion(s)
    '''
