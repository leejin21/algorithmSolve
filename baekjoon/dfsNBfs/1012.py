# 유기농 배추
# 그래프, bfs dfs
'''
문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

SOLUTION

TRY 1에서
0 0 0
0 1 1

0 0 1
0 0 1
---여기까지 다 괜찮음--
아래 특수한 경우가 적용 안됨.
<반례>
0  0 0 1
0  0 1 1
0 '1 1 1

1
4 3 6
3 0
2 1
3 1
1 2
2 2
3 2

그런데 그래도 안됨....

TRY 2

그냥 그래프로 구하기. 
대신 이번에는 dfs와 visited를 이용해서 미리 "이 지점에 field가 1이면 같은 그룹입니다"를 표시해두는 거임.
https://velog.io/@jengyoung/baekjoon1012 참고

'''

import sys

def dfs(x, y):
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx>=N or nx<0 or ny>=M or ny<0 or visited[nx][ny]:
            continue
        if ground[nx][ny] != 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

sys.setrecursionlimit(10**5)
read = sys.stdin.readline
T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())
    ground = [[0]*M for n in range(N)]
    visited = [[0]*M for n in range(N)]
    bug = 0

    for k in range(K):
        x, y = map(int, read().split())
        ground[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] and not visited[i][j]:
                visited[i][j] = 1
                bug += 1
                dfs(i, j)
    print(bug)