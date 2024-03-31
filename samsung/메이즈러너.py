'''
N = 격자의 변길이, M = 참가자
i초일 때(i<K)

이동
움직인 칸은 현재 머물러 있는 칸보다 출구까지의 최단 거리가 가까워야 함(출구와 가까워지는 거리)
상하 > 좌우
한칸에 두명 이상 있을 수 있음.
<출구 찾는 경우>
-1 -1으로 처리

미로 회전 범위 선택
- 한명 이상의 참가자, 출구 포함 가장 작은 정사각형
- (참가자, 출구): |참가자r - 출구r| + |참가자c - 출구c|
- 가장 작은 크기 갖는 정사각형 2개 이상 -> 좌상단 r좌표 작 > 좌상단 c좌표 작
: 비교는 1순위 - min<참가자r, 출구r>, 2순위 - min<참가자c, 출구c>

미로 회전
- 잡힌 곳 내구도 1씩 깎음(>0 인 경우만 1씩 깎아)
- 시계 방향으로 90도 회전

<방법>
r,c, R,C
인덱스 기반 [r][c] 값-> [C-c+1][r]의 자리로 가게 됨
<주의>
참가자도 옮기기(해당하는)
출구도 옮기기

(r,c)

1 2 3
4 5 6
7 8 9

(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)

7 4 1
8 5 2
9 6 3

(3,1) (2,1) (1,1)
(3,2) (2,2) (1,2)
(3,3) (2,3) (1,3)

'''
import sys; read = sys.stdin.readline
maze = []
participants = []
exit = []

def isEmptyRoad(r,c):
    if maze[r][c] == 0:
        return True
    return False
    
def checkIfArriveExit(pInfo, eInfo):
    p_r, p_c = pInfo
    e_r, e_c = eInfo
    if p_r == e_r and p_c == e_c:
        return True
    return False

def alreadyExited(pInfo):
    return pInfo[0] == -1 and pInfo[1] == -1

def moveParticipants(pInfo, eInfo):
    # pInfo = participant info = [r,c]
    # eInfo = exit info = [r,c]
    np_r, np_c = [-1, -1] # new location for participants
    p_r, p_c = pInfo
    e_r, e_c = eInfo
    upDownDetermin = False

    # 상하 결정
    if p_r < e_r: # 참가자가 더 위에 있는 경우
        if isEmptyRoad(p_r+1, p_c):
            np_r = p_r + 1
            upDownDetermin = True
    elif p_r > e_r: # 참가자가 더 아래에 있는 경우
        if isEmptyRoad(p_r-1, p_c):
            np_r = p_r - 1
            upDownDetermin = True
    
    # 좌우 결정
    if not upDownDetermin:
        if p_c < e_c: #참가자가 더 왼쪽에 있는 경우
            if isEmptyRoad(p_r, p_c+1):
                np_c = p_c + 1
        elif p_c > e_c: #참가자가 더 오른쪽에 있는 경우
            if isEmptyRoad(p_r, p_c-1):
                np_c = p_c - 1
    
    return np_r, np_c    

def prettyPrint(pList):
    for p in pList:
        for i in p:
            print(i, end = ' ')
        print()

def getRangeToRotate(eInfo):
    '''
    포함한: 가장 작은 정사각형 범위 정하기 -> 좌상단, 우하단 좌표
    포함으므로 max(세로길이, 가로길이) 중 골라서
        세로인 경우: abs(p_r - e_r)
        가로인 경우: abs(p_c - e_c) -> 좌상단 = ()

    가로=|p_r-e_r|, 세로=|p_c-e_c|
    좌상단 == 출구
        (1) 세로 > 가로
            우하단 r = e_r + |p_c - e_c|
            우하단 c = p_c
        (2) 세로 < 가로
            우하단 r = p_r
            우하단 c = p_c - |p_r - e_r|

    좌상단 != 출구
        (1) 세로 > 가로
            좌상단 r = e_r - |p_c - e_c|
            좌상단 c = p_c
        (2) 세로 < 가로
            좌상단 r = p_r
            좌상단 c = p_c + |p_r - e_r|
    '''
    
    e_r, e_c = eInfo
    minSR = 20; minSC = 20
    minSquareLen = 20
    for pIdx, part in enumerate(participants):
        p_r, p_c = part
        if e_c < p_c || (e_c == p_c && e_r < p_r):
            # 좌상단 == 출구
            pass
        else:
            # 좌상단 != 출구
            pass


def solution(K):
    time = 0
    while(time < K):
        # 1. 이동
        for pInfo in participants:
            if alreadyExited(pInfo):
                # participant already exit
                continue
            moveParticipants(pInfo, exit)
            if checkIfArriveExit(pInfo, exit):
                pInfo[0] = -1; pInfo[1] = -1
        
        # prettyPrint(participants)
        # 2. 미로 회전
        
        
        time += 1

N, M, K = [int(i) for i in read().split()]
for i in range(N):
    maze.append([int(i) for i in read().split()])

for i in range(M):
    participants.append([int(i)-1 for i in read().split()])

exit = [int(i)-1 for i in read().split()]

# print(maze)
# print(participants)
# print(exit)

solution(K)
