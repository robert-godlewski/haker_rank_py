# Strings solved in Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'pangrams' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# My code - Solved in 1 hr
def pangrams(s):
    print(f"inputed s = {s}")
    count = [0] * 26
    print(f"letter count at start = {count}")
    sArr = s.split(" ")
    print(f"splitted s = {sArr}")
    for i in sArr:
        wArr = list(i)
        print(f"splitted word = {wArr}")
        for j in wArr:
            if j == 'a' or j == 'A': count[0] += 1
            elif j == 'b' or j == 'B': count[1] += 1
            elif j == 'c' or j == 'C': count[2] += 1
            elif j == 'd' or j == 'D': count[3] += 1
            elif j == 'e' or j == 'E': count[4] += 1
            elif j == 'f' or j == 'F': count[5] += 1
            elif j == 'g' or j == 'G': count[6] += 1
            elif j == 'h' or j == 'H': count[7] += 1
            elif j == 'i' or j == 'I': count[8] += 1
            elif j == 'j' or j == 'J': count[9] += 1
            elif j == 'k' or j == 'K': count[10] += 1
            elif j == 'l' or j == 'L': count[11] += 1
            elif j == 'm' or j == 'M': count[12] += 1
            elif j == 'n' or j == 'N': count[13] += 1
            elif j == 'o' or j == 'O': count[14] += 1
            elif j == 'p' or j == 'P': count[15] += 1
            elif j == 'q' or j == 'Q': count[16] += 1
            elif j == 'r' or j == 'R': count[17] += 1
            elif j == 's' or j == 'S': count[18] += 1
            elif j == 't' or j == 'T': count[19] += 1
            elif j == 'u' or j == 'U': count[20] += 1
            elif j == 'v' or j == 'V': count[21] += 1
            elif j == 'w' or j == 'W': count[22] += 1
            elif j == 'x' or j == 'X': count[23] += 1
            elif j == 'y' or j == 'Y': count[24] += 1
            elif j == 'z' or j == 'Z': count[25] += 1
        print(f"current count = {count}")
    is_pangram = True
    for i in count:
        if i == 0:
            is_pangram = False
            break
    if is_pangram: return "pangram"
    else: return "not pangram"

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()
    '''
    # Testing pangrams
    s1 = "We promptly judged antique ivory buckles for the next prize"
    s1a = pangrams(s1)
    print(s1a)
    s2 = "We promptly judged antique ivory buckles for the prize"
    s2a =pangrams(s2)
    print(s2a)
