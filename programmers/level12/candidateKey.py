# 후보키, 틀림

'''
유일성, 최소성

학번
이름
전공
학년

학번 이름
학번 전공
학번 학년
이름 전공
이름 학년
전공 학년

'''

import collections

CNT = 0


def solution(relation):
    answer = 0
    rt = [list(x) for x in zip(*relation)]
    cand = []

    
    col_len = len(relation[0])
    row_len = len(relation)
    # print(rt, col_len)
    def findCandKey(i):
        global CNT
        for j in range(col_len-i+1):
            # counter = collections.Counter(rt[i:j])
            # print(j,j+i)
            counter = collections.Counter()
            for r in range(row_len):
                l = ['*']*(j-0) + relation[r][j:j+i] + ['*']*(col_len-(j+i))
                key = '-'.join(l)
                counter.update([key])
                
            # print(counter.most_common(1))
            exists = False
            if counter.most_common(1)[0][1] == 1:
                for c in cand:
                    if (j == c[0] and i+j >= c[1]) or (j <= c[0] and i+j == c[1]):
                        exists = True
                        break
                # 해당 후보키는 끝
                if not exists:
                    cand.append((int(j), int(j+i)))
                    # print(cand)
                    # print("끝")
                    CNT += 1
                # break

    for i in range(1, col_len+1):
        # i개 컬럼을 가지는 후보키 찾기
        findCandKey(i)
    
    return CNT

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))