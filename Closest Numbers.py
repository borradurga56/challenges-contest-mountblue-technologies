#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr): 
    output = []
    arr = sorted(arr)
    nowmin = 10**9
    
    for ind in range(1, len(arr)):
        diff = abs(arr[ind-1] - arr[ind])
        
        if diff < nowmin:
            output = [(arr[ind-1], arr[ind])]
            nowmin = diff
        elif diff == nowmin:
            output.append((arr[ind-1], arr[ind]))
            
    flat_list = [item for sublist in output for item in sublist]
        
    return flat_list
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
