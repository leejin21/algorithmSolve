'''

개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.
    대기실은 5개이며, 각 대기실은 5x5 크기입니다.
    거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
    단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
예를 들어,


SOLUTION
만약 P이면 이웃에 있는 P를 탐색하고: (둘 다) visited 표시하기
if 없으면 다음으로.
if 있으면:
    대각선 방향인 경우(1,1): 위, 옆 모두 X인 경우-continue, else-return 0
    일자 방향인 경우(2,0): 해당 방향: X인 경우-continue, else-return 0
    일자 방향인 경우(1,0): 그냥 return 0


(1,1)
(0,1), (1,0)
(1,-1)
(1,0), (0, -1)

[[
"POOOP", 
"OXXOX", 
"OPXPX", 
"OOXOX", 
"POXXP"], 
[
"POOPX", 
"OXPXP", 
"PXXXO", 
"OXXXO", 
"OOOPP"], 
[
"PXOPX", 
"OXOXP", 
"OXPXX", 
"OXXXP", 
"POOXX"], 
[
"OOOXX", 
"XPOXX", 
"OPOXX", 
"OXOOX", 
"OOOOO"], 
[
"PXPXP", 
"XPXPX", 
"PXPXP", 
"XPXPX", 
"PXPXP"]]


'''
LEN = 5
visited = [[False]*LEN for _ in range(LEN)]


def solution(places):
    global LEN, visited
    answer = []; success = True; 
    neighbor = [(2,0), (0,2), (-2,0), (0,-2), (1,1), (1,-1), (-1,1), (-1,-1), (1,0), (0,1), (-1,0), (0,-1)]
    for place in places:
        visited = [[False]*LEN for _ in range(LEN)]
        success = True
        for i in range(LEN):
            # i가 y축
            for j in range(LEN): 
                # j가 x축
                if place[i][j] == 'P':
                    visited[i][j] = True  
                    for n in neighbor:
                        # 일자 방향인데 거리=2
                        if isPerson(i+n[0], j+n[1], place):
                            visited[i+n[0]][j+n[1]] == True
                            success = checkDistanceRight(i, j, n[0], n[1], place)
                            if not success: break
                if not success: break
            if not success: break
        answer.append(0 if not success else 1)
                

    return answer

def checkDistanceRight(i, j, di, dj, place):
    pair = (abs(di), abs(dj))
    if pair == (0,2) or pair == (2,0):
        # 일자 방향인데 거리=2
        if place[i+di//2][j+dj//2] == 'O':
            # 가운데가 책상
            return False
    elif pair == (1,1):
        # 대각선 방향, 거리=2 또는 일자 방향, 거리=1
        if place[i+di][j] == 'O' or place[i][j+dj] == 'O':
            return False
    elif pair == (0,1) or pair == (1,0):
        # 대각선 방향, 거리=2 또는 일자 방향, 거리=1
        return False
        
    return True

def isPerson(x,y, place):
    global LEN, visited
    if not (0<=x<LEN and 0<=y<LEN):
        return False
    return (visited[x][y]==False and place[x][y] == 'P')



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))