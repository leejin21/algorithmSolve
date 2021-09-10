# 11:50 - 12:42
# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
'''
1. a와 b가 모두 공집합인 경우: 1
2. 다중집합 고려
3. 특수문자 -> 공백으로 처리 후 없애기(replace로 처리하기)
'''
import collections
import itertools

def preprocess(x):
    x = x.lower(); y = []
    i = 0
    for a in x:
        if i == 0:
            pre = a
            i+= 1
            continue
        cand = pre+a
        if (ord('a') <= ord(cand[0]) <= ord('z')) and (ord('a') <= ord(cand[1]) <= ord('z')):
            y.append(cand)
        pre = a
        i += 1
        
    return y

def solution(str1, str2):
    l1 = preprocess(str1)
    l2 = preprocess(str2)
    
    c1 = collections.Counter(l1)
    c2 = collections.Counter(l2)

    intersect = c1 & c2
    union = c1 | c2

    tot1 = 0; tot2 = 0
    for k1, v1 in intersect.items():
        tot1 += v1
    for k2, v2 in union.items():
        tot2 += v2
    answer = (tot1 / tot2) if tot2 > 0 else 1
    return int(answer*65536)

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
# print(solution('aa1+aa2', 'E=M*C^2	'))
# print(solution('aa1+aa2', ''))
