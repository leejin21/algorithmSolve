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


[진짜 반례]
11
10 20 10 30 20 21 22 23 24 25 50 
-> 10 20 21 22 23 24 25 50: 8


부분 수열이므로 어떻게던 가능하다.

시드를 박아둬야 함.
시드의 조건: 직전보다 작아야 함, 등장한 시드들과 비교했을 떄 가장 작은 값.

A_수열 = {1, 2, 1, 3, 2, 4}

재귀 써서 여러 경우로 생각해야 함.



'''
import sys; read = sys.stdin.readline
N = int(read())
A = list(map(int, read()[:-1].split()))

parts = []

def getLongPartNums():
    pass

for i in range(len(A)):
    # change = False
    if i == 0:
        parts.append([A[i], 1])
        continue
    for j, p in enumerate(parts):
        if A[i] > p[0]:
            parts[j][0] = A[i]; parts[j][1] += 1
            # change = True
        # elif A[i] == p[0]:
        #     change = True
    parts.append([A[i], 1])
        
parts.sort(key=lambda x: x[1], reverse=True)
print(parts)
print(parts[0][1])