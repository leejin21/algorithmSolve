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

<<TRY 1>>
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

<<TRY 2>>

'''

import collections, itertools

def solution(relation):
    answer = [0]
    pairs = []
    columns = ''.join([str(i) for i in range(len(relation[0]))])
    for cnt in range(len(relation[0])):
        for it in list(itertools.combinations(columns, cnt+1)):
            EXIST = False
            for i in range(1, len(it)+1):
                # i: 조합의 결과쌍의 길이
                for j in list(itertools.combinations(''.join(it), i)):
                    # j: 조합
                    if ''.join(j) in pairs:
                        EXIST = True
                        break
                if EXIST:
                    break

            if not EXIST:
                # 해당 컬럼 집합이 후보키가 될 수 있는 지 확인
                col_idxs = [int(i) for i in it]
                accum = []
                for i in col_idxs:
                    add = list(map(lambda x:x[i], relation))
                    if len(accum) == 0:
                        new_accum = add
                    else:
                        new_accum = []
                        for j in range(len(accum)):
                            new_accum.append(accum[j]+'-'+add[j])
                    accum = new_accum
                if collections.Counter(accum).most_common(1)[0][1] <= 1:
                    answer[0] += 1
                    pairs += [''.join(i) for i in list(itertools.permutations(''.join(it), len(it)))]
                    # TODO pair += 어쩌구
                    
    return answer[0]

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","math","4"]]))