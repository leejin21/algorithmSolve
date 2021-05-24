'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.


SOLUTION

[반례1]
11
10 20 10 30 20 21 22 23 24 25 50 
-> 10 20 21 22 23 24 25 50: 8

부분 수열이므로 어떻게던 가능하다.
재귀 써서 여러 경우로 생각해야 함.

[반례2]
11
10 50 10 50 1 2 3 4 10 50 10

원래 답: [2, 1, 2, 1, 6, 5, 4, 3, 2, 1, 1], 6
틀린 답: [1, 0, 1, 0, 5, 4, 3, 2, 1, 0, 1], 5

알고 보니까 10 50 10과 같은 부분에서 각각 [2 1 1]이 되어야 하는데 [1 0 1]처럼 됨.
이는 A[i]가 나머지보다 모두 큰 경우일 때 A[i]>A[j]만 걸려서 from_behind가 계속 0으로 값이 유지되기 떄문.
이런 경우: 즉 계속 0으로 남아있는 경우 1로 값을 갱신시켜줘서 이를 방지함.

++ 교훈 및 TIP: 내가 반례 찾아내는 과정에서 리스트 크기 잘 못 세는 경우가 허다하니까 그냥 파이썬에게 len으로 계산하게 하기..
이걸로 삽질하면 너무 아깝잖아..

'''
import sys; read = sys.stdin.readline
sys.setrecursionlimit(10000)

def getLongPartNums(i):
    if from_behind[i]:
        return from_behind[i]
    for j in range(i+1, len(A)):
        if A[i] == A[j]:
            continue
        elif A[i] > A[j]:
            getLongPartNums(j)      # 새로 시작!
        elif A[i] < A[j]:
            from_behind[i] = max(from_behind[i], getLongPartNums(j) + 1)
    if not from_behind[i]: from_behind[i] = 1
        # 진짜 반례 2에서 유추해낸 코드
    return from_behind[i]
    
N = int(read())
A = list(map(int, read()[:-1].split()))
from_behind = [0]*(len(A)-1)+[1]

getLongPartNums(0)
print(max(from_behind))