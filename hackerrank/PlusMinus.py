#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ratios = {'pos':0, 'zero':0, 'neg':0}
    for a in arr:
        if a > 0:
            ratios['pos']+= 1
        elif a == 0:
            ratios['zero']+=1
        else:
            ratios['neg']+=1
    # print(ratios)
    for i in [ratios['pos']/len(arr), ratios['neg']/len(arr), ratios['zero']/len(arr)]:
        print("{:0.5f}".format(i)) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
