# 메뉴리뉴얼
# 10:11 ~ 11:11

'''
python 중에 조합이 있는 지 알아 보기

course는 오름차순으로 정렬되어있음.

'''
import collections
import itertools


def solution(orders, course):
    # comb = [[[] for j in range(21)] for i in range(11)]
    comb = [collections.defaultdict(list) for i in range(11)]
    max_comb_cnt = [0]*11
    dd = collections.defaultdict(int)
    for order in orders:
        sorted_o = ''.join(sorted([i for i in order]))
        for i in range(2, len(order)+1):
            for p in list(itertools.combinations(sorted_o, i)):
                # print(''.join(p))
                dd[''.join(p)] += 1
    # print(dd)
    for k, v in dd.items():
        if max_comb_cnt[len(k)] <= v and v >= 2:
            max_comb_cnt[len(k)] = v
            comb[len(k)][v].append(k)
    answer = []
    # print(comb, max_comb_cnt)
    for c in course:
        answer+=comb[c][max_comb_cnt[c]]
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))