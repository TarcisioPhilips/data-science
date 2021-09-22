#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    arrayDict = Counter()
    freq = Counter()
    output=[]
    for q, value in queries:
            if q==1:
                freq[arrayDict[value]]-=1
                arrayDict[value]+=1
                freq[arrayDict[value]]+=1
            if q==2:
                if arrayDict[value]>0: 
                    freq[arrayDict[value]]-=1
                    arrayDict[value]-=1
                    freq[arrayDict[value]]+=1
            if q==3:
                if freq[value]>0:
                    output.append(1)
                else:
                    output.append(0)
    return output
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
