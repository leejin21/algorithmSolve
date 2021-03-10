'''
문제
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

[PriorityQueue]
* queue에 있는 PriorityQueue
* 디폴트 사이즈는 무한대
* put: 원소 추가
* get: root 원소 삭제
* 정렬 기준 변경: (우선순위, 값)으로 put하기
=> priority que 시간 초과남.

[heapq]
* 특이함. 
https://www.daleseo.com/python-heapq/  :여기 참고하기
'''

from queue import PriorityQueue

import heapq
import sys

# 일단 온라인 알고리즘으로 풀어보기.

def main():
    N = int(input())
    q = []; ans = []
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            # 큐에서 rootpop하고 print
            if len(q) == 0:
                ans.append(0)
            else:
                ans.append(-1 * heapq.heappop(q))
        else:
            # 큐에 insert
            heapq.heappush(q, -1*x)

    for x in ans:
        print(x)

main()