#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    clock12 = s[:-2]; t = s[-2:]
    clock12_list = [int(i) for i in clock12.split(":")]
    if t == 'PM' and clock12_list[0]!=12:
        clock12_list[0] += 12
    elif t == 'PM' and clock12_list[0] == 12:
        pass
    elif t == 'AM' and clock12_list[0] == 12:
        clock12_list[0] = 0
    clock24_list = ['%02d'%i for i in clock12_list]
    return ':'.join(clock24_list)

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
