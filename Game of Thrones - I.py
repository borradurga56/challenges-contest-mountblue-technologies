#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    counts = []
    for c in alpha:
        counts.append(s.count(c))

    counts = list(filter(lambda x: x%2!=0,counts))

    if len(counts)>1:
        return 'NO'

    else:
        return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
