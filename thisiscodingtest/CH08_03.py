# CH08 다이나믹 프로그래밍 - 03. 개미 전사


import sys; read = sys.stdin.readline

# 1. 탑다운: 재귀로 구현
def dp_topdown(num):
    print(num)
    if num == len(storage)-1:
        return storage[-1]
    elif num > len(storage)-1:
        return 0

    return max(dp(num+2) + storage[num], dp(num+1))

# 1. 탑다운: 메모이제이션 기법 추가
def dp_topdown_memo1(num):
    print(num)
    if num == len(storage)-1:
        return storage[-1]
    elif num > len(storage)-1:
        return 0
    
    if memo[num] != -1:
        return memo[num]

    memo[num] = max(dp(num+2) + storage[num], dp(num+1))
    return memo[num]

# 2. 바탐업: 왼쪽 -> 오른쪽으로 구하고 오른쪽이 최종 결과값으로.
def dp_bottomup():
    memo[0] = storage[0]
    memo[1] = max(storage[0], storage[1])

    for i in range(2, len(storage)):
        memo[i] = max(memo[i-1], memo[i-2]+storage[i])

    return memo[-1]


N = int(read().rstrip())
storage = [int(i) for i in read().rstrip().split(" ")]
memo = [-1]*len(storage)

print(dp_bottomup())

'''
최소한 한 칸 이상 떨어진 식량창고 약탈해야 함

메모이제이션 사용

An : n번째 위치부터 약탈할 수 있는 최대 식량 
an: n번째 식량창고의 보유 식량

An = max(A(n+2) + an, A(n+1))

4     
1 3 1 5
'''