#!/bin/python3
# 미완

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranking = []; cnt = 1
    for i in range(len(ranked)):
        if i>0 and ranked[i] < ranked[i-1]:
            cnt += 1
        ranking.append(cnt)
            
    IDX = len(ranked)-1
    pi = 0
    player_rank = []
    while(pi<len(player) and IDX>=0):
        if player[pi] < ranked[IDX]:
            player_rank.append(ranking[IDX]+1)
            pi += 1
        elif player[pi] == ranked[IDX]:
            player_rank.append(ranking[IDX])
            pi += 1
        else:
            IDX -= 1
    while(pi<len(player)):
        player_rank.append(1)
        pi += 1
    return player_rank

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)