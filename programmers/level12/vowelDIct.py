# 모음 사전
'''
선형 시간
규칙 얼른 찾아내서 나머지에 적용하기

'''
import sys; read = sys.stdin.readline
import collections

# class Node:
#     def __init__(self, alp):
#         self.alp = alp
#         self.num = 0
#         self.link = []
tot = 0

def solution(word):
    # A, AA, AAA, ...
    tot_lst = [0]*5
    
    def setTot_lst(level):
        if level == 4:
            tot_lst[level] = 1
        else:
            setTot_lst(level+1)
            tot_lst[level] = 1 + 5*tot_lst[level+1]

    def dfs(level):
        # 공백 문자 고려하기
        global tot
        if level < len(word):
            alp_list = ['A', 'E', 'I', 'O', 'U']
            for n in alp_list:
                if word[level] == n:
                    tot += 1
                    dfs(level+1)
                    break
                else: tot += tot_lst[level]
    
    setTot_lst(0)
    dfs(0)
    return tot

# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
print(solution("EIO"))