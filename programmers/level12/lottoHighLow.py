# 로또의 최고 순위와 최저 순위
from collections import defaultdict



def solution(lottos, win_nums):
    ranks = {6:1, 5: 2, 4:3, 3:4, 2:5, 1:6, 0:6}
    lottos_dict = defaultdict(int)
    cnt = 0
    for i in lottos:
        lottos_dict[i] += 1
    for w in win_nums:
        if lottos_dict[w] > 0:
           cnt += 1
    
    return [ranks[cnt+lottos_dict[0]], ranks[cnt]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))