# 미완
import math
import os
import random
import re
import sys
import collections, copy
'''
5
ab
bb
hefg
dhck
dkhc

'''
# 바이너리 서치 해야 함!!

def biggerIsGreater(w):
    # Write your code here
    # alpList = sorted(list(set([i for i in w])))
    # print([i for i in w])
    
    # print(alpList)
    FIND = [False]; REALFIND = [False]; answer = ['no answer']
    def dfs(word, d):
        if len(word) == len(w):
            # END OF THE WORD
            # print(word)
            # 종결 조건
            if w == word:
                FIND[0] = True
            elif w < word and FIND[0] == True:
                # 찐 정답 찾음
                REALFIND[0] = True
                answer[0] = word
            # FIND = None, FIND = True 적기
            # print(FIND, REALFIND, answer)
            return
        for i, r in enumerate(alp_sorted):
            # 선택하는 건 alpDict의 cnts로 선택
            if REALFIND[0]:
                return
            # 이슈: remains를 어떻게 해서 보내 줄 것인가?
            if d[r] > 0:
                copy_dict = copy.deepcopy(d)
                copy_dict[r] -= 1
                dfs(word+r, copy_dict)

    wCounter = collections.Counter(w)
    alpDict = dict(wCounter)
    alp_sorted = sorted(alpDict.keys())
    for i, alp in enumerate(alp_sorted):
        # 선택하는 건 alpDict의 cnts로 선택, 선택되면 cnt-1 해주고, cnt>0일때만 선택.
        if not REALFIND[0]:
            copyDict = copy.deepcopy(alpDict)
            copyDict[alp] -= 1
            dfs(alp, copyDict)
    
    return answer[0]

T = int(input().strip())

for T_itr in range(T):
    w = input()
    print(biggerIsGreater(w))