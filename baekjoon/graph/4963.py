# 섬의 개수
import sys; read = sys.stdin.readline


def visitNear(i, j):
    global guidance
    if 0<=i<len(guidance) and 0<=j<len(guidance[0]) and guidance[i][j]:
        guidance[i][j] = 0
        # 가로 세로
        visitNear(i+1, j)
        visitNear(i-1, j)
        visitNear(i, j+1)
        visitNear(i, j-1)
        # 대각선
        visitNear(i+1, j+1)
        visitNear(i-1, j+1)
        visitNear(i+1, j-1)
        visitNear(i-1, j-1)

sys.setrecursionlimit(10000)

answer = []
while(True):
    w, h = list(map(int, read()[:-1].split(" ")))
    if w == 0 and h == 0: break
    guidance = []
    for _ in range(h):
        guidance.append(list(map(int, read()[:-1].split(" "))))

    cnt = 0
    for i in range(len(guidance)):
        for j in range(len(guidance[0])):
            if guidance[i][j]: 
                visitNear(i, j)
                cnt += 1
                # print(guidance)
    answer.append(cnt)

for a in answer:
    print(a)