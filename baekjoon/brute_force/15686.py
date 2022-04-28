# 백준: 치킨 배달
'''
치킨 거리 = 집 ~ 가장 가까운 치킨집 거리
도시의 치킨 거리 = 모든 치킨 거리의 합

0 빈 칸 1 집 2 치킨집

1 <= 집의 개수 < 2N
M <= 치킨집의 개수 <= 13

N = 인풋 줄의 개수(배열)
M = 폐업시키지 않을 치킨집을 최대 M개로 고르기
-> "도시의 치킨 거리의 최솟값" 구하기

[풀이]: 브루트 포스

combinations로 치킨집 조합 구한 후 
    각 조합별 집 기준 ~ 치킨집 최소 거리 구해서 해당 조합에서의 도시의 치킨 거리 구하기
    그 중 가장 작은 도.치.거를 가지는 조합에서의 도.치.거를 리턴

'''
from itertools import combinations
import sys

def main(M, city):
    # 미리 치킨, 집 위치 찾기
    markets = []; houses = []
    for i in range(len(city)):
        for j in range(len(city)):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                markets.append((i, j))
    
    market_combination = combinations(range(len(markets)), M)
    getDistance = lambda i1, j1, i2, j2: abs(i2-i1)+abs(j2-j1)
    min_city_chicken_dist = sys.maxsize

    for comb in market_combination:
        city_chicken_dist = 0
        for h in houses:
            hi, hj = h
            # print([comb for comb in market_combination])
            city_chicken_dist += min([getDistance(hi, hj, markets[c][0],  markets[c][1]) for c in comb])
        
        min_city_chicken_dist = min(city_chicken_dist, min_city_chicken_dist)
        # print(city_chicken_dist, min_city_chicken_dist)
            
    return min_city_chicken_dist

# 입력 부분
N, M = [int(i) for i in input().split(" ")]
city = [[int(i) for i in input().split(" ")] for _ in range(N)]

print(main(M, city))
