import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j + 1] :
                a[j], a[j + 1] = a[j + 1], a[j]
                count+=1
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))

    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)