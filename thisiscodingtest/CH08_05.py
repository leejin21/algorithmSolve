# CH08 - 05. 효율적인 화폐 구성
import sys; read = sys.stdin.readline

# TOP-DOWN
def dp_memo(remain, cnt):
    MIN = 1000
    if remain == 0:
        d[remain] = cnt
        return cnt
    elif remain < 0:
        return MIN

    if d[remain] != -1:
        return d[remain]
    
    for i in range(len(money_value)):
        MIN = min(MIN, dp(remain-money_value[i], cnt+1))

    d[remain] = MIN
    return MIN


def dp(remain, cnt):
    MIN = 1000
    if remain == 0:
        return cnt
    elif remain < 0:
        return MIN

    for i in range(len(money_value)):
        MIN = min(MIN, dp(remain-money_value[i], cnt+1))

    return MIN

# BOTTOM_UP
def dp_bottomup():
    

N, M = [int(i) for i in read().rstrip().split(" ")]
money_value = [int(read().rstrip()) for i in range(N)]
d = [-1] * (M+1)

# ans = dp(M, 0)
dp_memo(M, 0)
ans = d[M]

if ans == 1000:
    print(-1)
else:
    print(ans)

'''
화폐 개수를 최소한으로 이용해서 그 가치의 합이 M이 되도록 하는 경우

화폐 1: 0, 1, 2, 3... 개 사용하는 경우
화폐 2: 0, 1, 2, 3 ... 개 사용하는 경우

-> 이렇게 나누는 경우, 시간 복잡도 넉넉할까?

혹은 

Atot = max(A(tot-화폐1)+1, A(tot-화폐2)+1, A(tot-화폐3)+1), ....)

2 15
2
3

-> 메모이제이션 추가 후 틀림.
수정 필요

'''