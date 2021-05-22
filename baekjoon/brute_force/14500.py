# 테트로미노 
'''
문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.


SOL

해당 칸을 포함했을 떄 나오는 모든 경우의 수 합 => 최댓값 계속 갱신,
해당 칸이 끝나는 경우 visit에서 true로 처리해 주기.

<반례>
i1.
8 8 8 4 5
8 2 3 2 1
1 1 1 1 1
6 5 1 1 1
1 2 8 1 1


i2.
8 8 1 4 5
8 2 3 2 1
8 1 1 1 1
6 5 1 1 1
1 2 8 1 1


i3.
8 8 1 4 5
1 8 8 2 1
1 1 1 1 1
6 5 1 1 1
1 2 8 1 1
'''

import sys; read = sys.stdin.readline

diff = {'l': [(0,-1), 'r'], 'r': [(0,1), 'l'], 'u': [(-1,0), 'd'], 'd':[(1, 0), 'u']}
diff2 = {'u': [(0,1), (-1,1), (0,2)], 'r': [(-1,0), (1,0), (0,1)], 'l': [(1,1), (0,1), (-1, 1)], 'd': [(0,1), (1,1), (0,2)], 'i1': [(0,1), (1,0), (2,0)], 'i2': [(0,1), (0,2), (1,0)], 'i3': [(0,1), (-1,1), (-1,2)]}

def getMaxSum(i, j, depth, cur_tot, overlap):
    global M, N, MAX
    # r, l, u, d
    # print(i, j)
    if i>=0 and j>=0 and i<N and j<M and not visit[i][j]:
        # print('i,j = ', i, j, 'depth=',depth, 'curtot=',cur_tot, 'cur=',paper[i][j])
        if depth < 3:
            for k, v in diff.items():
                if k != overlap:
                    di, dj = v[0]
                    # print(k)
                    getMaxSum(i+di, j+dj, depth+1, cur_tot+paper[i][j], v[1])
        elif depth == 3:
            MAX = max(MAX, cur_tot+paper[i][j])
            # print("...")
            # print(i, j, MAX, cur_tot+paper[i][j])
            # print("...")

def getMaxSum2(i, j):
    global N, M, MAX
    # ㅗ, ㅏ, ㅓ, ㅜ의 경우 커버하기(i, j가 무조건 가장 왼쪽 가운데, 따라서 visited 안 씀)
    # 위 반례1,2의 경우 커버하기: i, j가 왼쪽 위에 해당.
    for key, value in diff2.items():
        # print(key)
        tot = paper[i][j]
        interrupt = False
        for v in value:
            di, dj = v
            # print(i+di, j+dj)
            if 0<=i+di<N and 0<=j+dj<M:
                tot += paper[i+di][j+dj]
                # print(tot)
            else:
                interrupt = True
                # print("interrupt")
                break
        if not interrupt: MAX = max(MAX, tot)
        # print(MAX, tot)


MAX = -1000000
# N, M = list(map(int, read()[:-1].split()))
N = 5; M = 5
paper = list(map(lambda _: list(map(int, read()[:-1].split())), range(N)))
visit = [[False]*M for _ in range(N)]
# print(visit)
# getMaxSum(0,0, 0, 0, '')
# getMaxSum2(0,0)

for i in range(N):
    for j in range(M):
        getMaxSum(i, j, 0, 0, '')
        getMaxSum2(i, j)
        # 로직
        visit[i][j] = True

print(MAX)