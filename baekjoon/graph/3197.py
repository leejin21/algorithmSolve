# 백조의 호수
# 시간 초과, 미완
'''
0. 백조의 위치는 정해져 있음: 백조의 위치 찾아내기.
1. 백조들이 같이 있는 지 확인한다(같은 공간에 있는 지)
2. 호수를 매일 녹인다.
3. 1번 과정부터 다시 반복.
'''

'''
2 2
LX
XL

'''
import sys; read = sys.stdin.readline
import collections
import copy

sys.setrecursionlimit(1000000)

def solution(R, C, place):
    answer = 0
    together = False
    swan_cnt = [0]
    temp_place = None
    swan_pos = None
    # 0. find swans position O(n^2)
    for i in range(R):
        for j in range(C):
            if place[i][j] == 'L':
                swan_pos = (i,j)
                break

    def dfs(i, j):
        if i<0 or i>=R or j<0 or j>=C:
            return
        if temp_place[i][j] == 'X' or temp_place[i][j] == 'l':
            # this pos is ice or visited swan or visited water
            return
        if temp_place[i][j] == 'L':
            # this pos is swan(first time to visit)
            swan_cnt[0] += 1
            temp_place[i][j] = 'l'
        else:
            temp_place[i][j] = 'X'
            # note visited
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    while(not together):

        swan_cnt = [0]
        temp_place = copy.deepcopy(place)

        # 백조가 같은 물 세그먼트에 있는 지 확인
        dfs(swan_pos[0], swan_pos[1])

        if swan_cnt[0] == 2:
            together = True
            break

        # 얼음 녹이기
        for i in range(R):
            for j in range(C):
                if place[i][j] == 'X' and ((i<R-1 and place[i+1][j] == '.') or (i>0 and place[i-1][j] == '.') or (j>0 and place[i][j-1] == '.') or (j<C-1 and place[i][j+1] == '.')):
                    place[i][j] = 'x'
                elif place[i][j] == 'X' and ((i<R-1 and place[i+1][j] == 'L') or (i>0 and place[i-1][j] == 'L') or (j>0 and place[i][j-1] == 'L') or (j<C-1 and place[i][j+1] == 'L')):
                    place[i][j] = 'x'
        
        for i in range(R):
            for j in range(C):
                if place[i][j] == 'x':
                    place[i][j] = '.'
        
        answer += 1

    return answer

R, C = list(map(int, read()[:-1].split(' ')))
place = list(map(lambda i: [j for j in read()[:-1]], range(R)))
# print(place)
print(solution(R, C, place))