'''
숨바꼭질

문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

SOLUTION
BFS 이용해서 풀기

더 멀어지지 않는 방향으로 가기..?

5 17
5 -> 4, 6, 10
    4 -> 3, 5, 8
        3 -> 2 4 6
        5 -> 4 6 10
        8 -> 7 9 16
    6 -> 5, 7, 12
        5 -> 4 6 10
        7 -> 6 8 14
        12 -> 11 13 24
    10 -> 9 11 20

큐 이용
5
4 6 10
(6 10 3 5 8
10 3 5 8 5 7 12)
3 5 8 5 7 12 9 11 20
(5 8 5 7 12 9 11 20 2 4 6)
...

# TRY 1:
    메모리 초과, 아마 loc-1, loc+1, loc*2 모두 다 조건에 상관없이 떄려넣어서 그런 걸로 추측됨
# TRY 2:
    if loc -1 >= 0: q.append(loc-1)
    if loc +1 <=100000: q.append(loc+1)
    if loc * 2 <= 100000: q.append(loc*2)

    를 넣었는데도 메모리 초과 뜸.

# TRY 3:
    visited는 제외하기(최소로 가야하므로: 중복되는 경로 없어야 함!!)
'''
import sys; read = sys.stdin.readline
from collections import deque

N, K = tuple(map(int, read()[:-1].split(" ")))
q = deque([N]); sec = 0; find_ans = False
visited = [False]*100001

while(True):
    end = len(q); i = 0
    while(i<end):
        loc = q.popleft(); visited[loc] = True
        if loc==K: 
            find_ans = True; break
        if loc -1 >= 0 and not visited[loc-1]: q.append(loc-1)
        if loc +1 <=100000 and loc<K and not visited[loc+1]: q.append(loc+1)
        if loc * 2 <= 100000 and loc<K and not visited[loc*2]: q.append(loc*2)
        i += 1
    if find_ans: break
    sec += 1

print(sec)