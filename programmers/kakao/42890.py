# 후보키
# 후보키
'''
후보키는 최소성, 유일성을 만족.
재귀 이용해서
컬럼 1
    if 유일성 만족
        브레이크하고 parent로 올라간 후 다음: 컬럼 2로.
    else 유일성 만족 X
        다음: 컬럼1-컬럼2로.

그래서 만약 컬럼 1, 컬럼 2가 유일성 만족하지 않을 경우: 컬럼1-컬럼2-컬럼3으로 확인.


<반례>
[["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","math","4"]]
<이유>
tot_accum = [['100', '200', '300', '400', '500', '600'], ['ryan-music-2', 'apeach-math-2', 'tube-computer-3', 'con-computer-4', 'muzi-music-3', 'apeach-math-4'], ['ryan-2', 'apeach-2', 'tube-3', 'con-4', 'muzi-3', 'apeach-4'], ['music-2', 'math-2', 'computer-3', 'computer-4', 'music-3', 'math-4']]
최소성을 만족시키기 어려움.


'''

import sys
import collections

sys.setrecursionlimit(10000)
def solution(relation):
    answer = [0]
    tot_accum = []
    pairs = []
    def recursive(i, accum, accum_pair):
        # print(i, accum, answer)
        add = list(map(lambda x:x[i], relation))
        new_accum = []
        if len(accum) == 0:
            new_accum = add
        else:
            for j in range(len(accum)):
                new_accum.append(accum[j]+'-'+add[j])
        # print(new_accum)
        
        if collections.Counter(new_accum).most_common(1)[0][1] <= 1:
            tot_accum.append(new_accum)
            answer[0] += 1
            return
        else:
            for k in range(i+1, len(relation[0])):
                recursive(k, new_accum)
    for i in range(len(relation[0])):
        recursive(i, [])
    print(tot_accum)
    return answer[0]

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","math","4"]]))