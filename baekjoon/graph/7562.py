# 나이트의 이동
'''
나이트가 이동할 수 있는 방법: "BFS로, 큐로 이동"

i-2, j+1
i-1, j+2
i+1, j+2
i+2, j+1
i-2, j-1
i-1, j-2
i-1, j+2
i-2, j+1

(+-2, +-1)
(+-1, +-2)

방향 지정해 주기

BFS로 풀게 되면 큐로.

실수 조심: pop, popleft 구분, append, appendleft 구분하기

'''

import sys; read = sys.stdin.readline

sys.setrecursionlimit(100000)

from collections import deque


def move2DestBFS(cur_i, cur_j):
    q = deque([(cur_i, cur_j)])
    nightmoves = [(1, 2), (2,1)]
    
    while(q):
        i,j = q.popleft()
        if i == dest_i and j == dest_j:
            return
            # print(i, j, cnt)
            
        for x, y in [(1,-1), (-1, 1), (1,1), (-1,-1)]:
            for m in nightmoves:
                next_i = i+m[0]*x; next_j = j+m[1]*y
                    # print(next_i, next_j, chess[next_i][next_j])
                if (0<=next_i<len(chess)) and (0<=next_j<len(chess)) and (not chess[next_i][next_j]):
                    # print(next_i, next_j)
                    chess[next_i][next_j] = chess[i][j] + 1
                    q.append((next_i,next_j))
        # print(q)
        # for c in chess:
            # print(c)
        

T = int(read())
for _t in range(T):
    l = int(read())
    
    chess = [[0]*l for _ in range(l)]
    cur_i, cur_j = list(map(int, read()[:-1].split(" ")))
    dest_i, dest_j = list(map(int, read()[:-1].split(" ")))
    move2DestBFS(cur_i, cur_j)
    # for c in chess:
    #     print(c)
    print(chess[dest_i][dest_j])
    # i, j는 편의상 y, x축에서의 위치를 나타낸다고 생각하기
    