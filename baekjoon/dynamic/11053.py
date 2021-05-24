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

10 - 20 - 30 - 50 - : 50, 4
10 - 30 - 50 - : 50, 3
20 - 50 - : 50, 2

[반례]
12
50 60 70 80 10 20 30 40 50 60 70 80

10
1 1 1 1 1 2 2 2 2 2


[진짜 반례1]
11
10 20 10 30 20 21 22 23 24 25 50 
-> 10 20 21 22 23 24 25 50: 8

부분 수열이므로 어떻게던 가능하다.
재귀 써서 여러 경우로 생각해야 함.

[진짜 반례2]
11
10 50 10 50 1 2 3 4 10 50 10


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