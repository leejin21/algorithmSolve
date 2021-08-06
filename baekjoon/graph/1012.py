# 유기농 배추
import sys; read = sys.stdin.readline


sys.setrecursionlimit(100000)
ground = []

def searchCabbage(i, j):
    if 0<=i<len(ground) and 0<=j<len(ground[0]) and ground[i][j]:
        ground[i][j] = 0
        searchCabbage(i+1, j)
        searchCabbage(i-1, j)
        searchCabbage(i, j-1)
        searchCabbage(i, j+1)


T = int(read())
for _t in range(T):
    M, N, K = list(map(int, read()[:-1].split(" ")))
    ground = [[0]*M for _i in range(N)]
    worm_cnt = 0

    for _k in range(K):
        x, y = list(map(int, read()[:-1].split(" ")))
        ground[y][x] = 1

    # for g in ground:
    #     print(g)

    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if ground[i][j]:
                searchCabbage(i, j)
                worm_cnt += 1
                # for g in ground:
                #     print(g)
                # print()

    print(worm_cnt)