# Practice Test Aug 2022
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'fizzBuzz' function below.
# The function accepts INTEGER n as parameter.
# My Solution - About 8 min or so
def fizzBuzz(n):
    i = 1
    word = ""
    while i <= n:
        if i % 3 == 0: word += "Fizz"
        if i % 5 == 0: word += "Buzz"
        if word == "": print(i)
        else: print(word)
        word = ""
        i += 1

if __name__ == '__main__':
    '''
    n = int(input().strip())
    fizzBuzz(n)
    '''
    print("Fizzbuzz 15:")
    print(fizzBuzz(15))
