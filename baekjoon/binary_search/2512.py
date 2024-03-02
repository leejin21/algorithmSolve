# 2512
# Silver 2
# 예산

'''
문제
국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

입력
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 

출력
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 


예제 입력 1
4
120 110 140 150
485

예제 출력 1
127


예제 입력 2
5
70 80 30 40 100
450

예제 출력 2
100


최대의 총 예산 구하기 <- 상한액 설정 필요
종료조건

'''
import sys
input = sys.stdin.readline

limitMax = 0
# limitMax = 0으로 초기화해도 되는 이유
# 조건: stt > end인데 매번 allocValue > M이어야 함

def getTotalAllocValue(limit):
    tot = 0
    for v in requests:
        if v > limit:
            tot += limit
        else:
            tot += v
    return tot

def binarySearch(stt, end):
    # mid = 이번 설정한 limit
    global limitMax

    if stt > end:
        return limitMax

    mid = stt + (end - stt)//2
    allocValue = getTotalAllocValue(mid)
        # 이번 설정한 limit으로 구한 배정할 예산

    if allocValue == M:
        return mid
    elif allocValue > M: 
        # 배정 예산 > 사용 가능 예산
        return binarySearch(stt, mid-1)
    else:
        # 배정 예산 < 사용 가능 예산  
        limitMax = mid if (limitMax < mid) else limitMax
        return binarySearch(mid+1, end)


def answer():
    totalRequested = sum(requests)
    if totalRequested <= M:
        # 총 예산 >= 요청된 예산일 경우, 넉넉한 예산이므로 요청된 예산 모두 주면 될 듯
        return max(requests)
    else:
        return binarySearch(0, M)
    

N = int(input().rstrip())
requests = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
sys.setrecursionlimit(1000)

print(answer())