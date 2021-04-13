# 요세푸스 문제
'''
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력
예제와 같이 요세푸스 순열을 출력한다.

'''
import sys;read=sys.stdin.readline
from collections import deque

N, K = tuple(map(int, read().split(' ')))

q = deque(range(1,N+1))
josephus = []

def calCritPoint():
    # K%len(q)-1을 적용하면 (N,K)=(5,7)일 때 (5,2)와 동일한 결과임. 그런데 (N,K)=(3,3)일 때 그냥 K%len(q)-1을 하는 경우 while문을 지나치고 0번째 요소부터 pop함(원래 0번째 pop&append, 1번쨰 pop&append, 2번째 요소는 pop만 해야 함.)
    # 그런데 len(q)-1을 하면 이상하게 시간이 더 걸려서(약 100ms 정도 더) 그냥 K-1로 처리해 줌.
    return K%len(q)-1 if K%len(q)!=0 else K-1

while(len(q)>0):
    k = 0
    while(k<calCritPoint()):
        q.append(q.popleft()); k += 1
    josephus.append(q.popleft())

print('<', end='')
for i in range(len(josephus)):
    print(josephus[i], end=', ' if i<len(josephus)-1 else '>')