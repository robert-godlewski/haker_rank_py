# Array solved Aug 2022
# #!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'flippingBits' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
# My code - Solved in 1 hr
# Converts decimal numbers to binary numbers
def decimalBinary(dec, dec_str=""):
    #print(f"dec = {dec}")
    #print(f"dec_str = {dec_str}")
    if dec % 2 == 0: dec_str = "0" + dec_str
    else: dec_str = "1" + dec_str
    if dec <= 1: return int(dec_str)
    else: return decimalBinary(dec//2, dec_str)

# converting binary (array) to decimal number
def binaryDecimal(arr, num=0, i=0):
    val = arr.pop()
    if val == "1": num += (2**i)
    if arr: return binaryDecimal(arr, num, i=i+1)
    else: return num

def flippingBits(n):
    # Convert n to a binary number (base 2)
    print(f"The number at start = {n}")
    binN = decimalBinary(n)
    print(f"Binary of {n} = {binN}")
    binN_str = str(binN)
    while len(binN_str) < 32: binN_str = "0" + binN_str
    print(f"32 bit of {n} = {binN_str}")
    # flipping values
    binN_arr = list(binN_str)
    flipBin = ""
    i = 0
    while i < len(binN_arr):
        if binN_arr[i] == "0": 
            binN_arr[i] = "1"
            flipBin += "1"
        else: 
            binN_arr[i] = "0"
            flipBin += "0"
        i += 1
    binN_str = str(binN_arr)
    print(f"32 bit flipped version = {flipBin}")
    # Converting binary to decimal (base 10)
    num = binaryDecimal(binN_arr)
    print(f"Fliped number is = {num}")
    return num


if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
    '''
    # Testing code
    n1 = 9
    n1_flip = flippingBits(n1)
    ''''''
