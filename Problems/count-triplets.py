#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    counter = 0
    numbers = {}
    pairs = {}
    
    for i in reversed(arr):
        if r*i in pairs:
            counter += pairs[r*i]
        if r*i in numbers:
            pairs[i] = pairs.get(i,0) + numbers[r*i]
        
        numbers[i] = numbers.get(i,0) +1
    return counter
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
