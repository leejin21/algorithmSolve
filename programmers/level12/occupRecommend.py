# 직업군 추천
'''
언어 선호도 * 직업군 언어 점수의 총합이 가장 높은 직업군 return하기


꼴
JAVA: SI: 5, 이렇게.

'''
import sys; read = sys.stdin.readline
import collections

# sys.setrecursionlimit(10000)

def solution(table, languages, preference):
    occup_dict = collections.defaultdict(dict)
    pref_occup = collections.defaultdict(int)
    
    for t in table:
        t_lst = t.split()
        for i in range(len(t_lst)-1, 0, -1):
            occup_dict[t_lst[6-i]][t_lst[0]] = i
    
    for l, p in zip(languages, preference):
        for k, v in occup_dict[l].items():
            pref_occup[k] += v * p
    
    MAX_LANG = 0; MAX_POINT = 0
    for k, v in pref_occup.items():
        if MAX_POINT < v:
            MAX_LANG = k; MAX_POINT = v
        elif MAX_POINT == v and MAX_LANG > k:
            MAX_LANG = k
            
    return MAX_LANG

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"], [7, 5, 5] ))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))