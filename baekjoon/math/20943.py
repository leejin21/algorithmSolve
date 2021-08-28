'''
nC2 - aC2 - bC2 ...

기울기 구해서 딕셔너리 += 1
딕셔너리 아이템 중 밸류 >= 2인 것들은 밸류C2해서 nC2에서 빼 주기

기울기: -a/b


5
1 2 3
-1 -2 3
1 -2 3
1 0 1
2 0 1

'''
import sys; read = sys.stdin.readline
import collections

# sys.setrecursionlimit(10000)

def solution(N, straights):
    answer = N * (N-1) // 2
    inc_dict = collections.defaultdict(int)
    for straight in straights:
        a, b, c = straight
        inclination = -1 * a/b if b!= 0 else 'y_0'
        inc_dict[inclination] += 1
    #     print(a,b,inclination, inc_dict)
    # print(inc_dict)

    for key, value in inc_dict.items():
        if value >= 2:
            answer -= value * (value-1) // 2
            # print(key, value, answer)

    return answer

N = int(read())
straights = [list(map(int, read()[:-1].split(' '))) for i in range(N)]
print(solution(N, straights))