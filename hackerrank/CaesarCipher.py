#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    answer = ''
    k = k % 26
    for c in s:
        if ord('a')<=ord(c)<ord('z')-k+1:
            answer += chr(ord(c)+k)
        elif ord('z')-k+1<=ord(c)<=ord('z'):
            answer += chr(ord(c)-(ord('z')-k+1)+ord('a'))
        elif ord('A')<=ord(c)<ord('Z')-k+1:
            answer += chr(ord(c)+k)
        elif ord('Z')-k+1<=ord(c)<=ord('Z'):
            answer += chr(ord(c)-(ord('Z')-k+1)+ord('A'))
        else:
            answer += c
    return answer
    # Lipps_Asvph!
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
