# 프렌즈4블록
'''
프렌즈 4블록
45분 컷
'''

def solution(m, n, board):
    answer = 0
    transBoard = list(map(lambda x: list(x), list(zip(*board))))
    # transpose해 주기: 대신 2차원 리스트 형태(그냥 list(zip(*board))는 튜플을 감싼 리스트 형태)[21]
    while(True):
        # 하나의 턴
        detectedBlocks = dict()
        for i in range(n):
            for j in range(m):
                if i<n-1 and j<m-1 and transBoard[i][j]:
                    if transBoard[i][j] == transBoard[i+1][j] == transBoard[i][j+1] == transBoard[i+1][j+1]:
                        detectedBlocks[str(i)+'-'+str(j)] = True
                        detectedBlocks[str(i)+'-'+str(j+1)] = True
                        detectedBlocks[str(i+1)+'-'+str(j)] = True
                        detectedBlocks[str(i+1)+'-'+str(j+1)] = True
        if len(detectedBlocks.keys()) == 0:
            break
        # print(len(detectedBlocks.keys()))
        for idxs in [i.split('-') for i in detectedBlocks.keys()]:
            x, y = map(int, idxs)
            transBoard[x][y] = None
            answer += 1
        # break
        # 붕 떠 있는 것들 내려주기
        for i in range(n):
            newList = [a for a in transBoard[i] if a]
            transBoard[i] = [None]*(m-len(newList))+newList
        # print(*transBoard)
        # break

    # print(transBoard)
    # print(len(transBoard), n)
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))