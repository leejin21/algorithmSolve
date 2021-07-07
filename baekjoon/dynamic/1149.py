# RGB 거리

'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

3
26 40 83
49 60 57
13 89 99


100 100 10
100 100 1
100 100 100




출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

시간 초과 뜸. 


'''
import sys; read = sys.stdin.readline

sys.setrecursionlimit(10000)

def colorHouse1(num, cost, pre_color):
    # 시간 초과
    global MIN
    if num >= len(cost_list):
        MIN = min(MIN, cost)
    else:
        for color in range(len(cost_list[0])):
            next_cost = cost+cost_list[num][color]
            if color != pre_color and next_cost<MIN:
                colorHouse1(num+1, next_cost, color)
            
def colorHouse():
    # 이런 경우 전 단계의 노드들이 3개로 정해져 있는 상태이므로, 그냥 직접 비교해주면 됨.
    color_list = [[0]*3 for i in range(len(cost_list))]
    color_list[0] = cost_list[0]
    
    for i in range(1, len(cost_list)):
        color_list[i][0] = cost_list[i][0] + min(color_list[i-1][1], color_list[i-1][2])
        color_list[i][1] = cost_list[i][1] + min(color_list[i-1][0], color_list[i-1][2])
        color_list[i][2] = cost_list[i][2] + min(color_list[i-1][0], color_list[i-1][1])
    print(min(color_list[-1]))

        
N = int(read())
cost_list = list(map(lambda x: list(map(int, read()[:-1].split())), range(N)))
MIN = 10000000
colorHouse()
print(MIN)
# print(color_list)