# String manipulation Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'caesarCipher' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
# My solution - Took about an hour because I didn't know how to check the ASCII character of letters - Still doesn't work
def caesarCipher(s, k):
    #print(f"message in = {s}")
    s_arr = list(s)
    #print(s_arr)
    result = ""
    for letter in s_arr:
        # a = 97, z = 122, A = 65, Z = 90
        #print(letter)
        acl = ord(letter)
        #print(acl)
        if acl < 65 or acl > 122:
            # not a letter
            pass
        elif acl > 90 and acl < 97:
            # again not a letter
            pass
        elif acl + k > 90 and acl + k < 97 or acl + k > 122:
            num = acl + k - 26
            #print(num)
            letter = chr(num)
        else:
            num = acl + k
            #print(num)
            letter = chr(num)
        #print(letter)
        result += letter
    return result

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
    '''
    s = "There's-a-starman-waiting-in-the-sky"
    print(s)
    encrypt = caesarCipher(s, 3)
    print(encrypt)
