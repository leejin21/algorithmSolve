# 가운데를 말해요
# refactoring not done: 어떻게 하면 더 짧은 코드로?
'''
문제
수빈이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 수빈이가 정수를 하나씩 외칠때마다 동생은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 수빈이가 외친 수의 개수가 짝수개(2n)라면 중간에 있는 두 수 중에서 작은 수(n-1번째)를 말해야 한다.

예를 들어 수빈이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 수빈이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 수빈이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 수빈이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 수빈이의 동생이 말해야하는 수를 순서대로 출력한다.

[SOLUTION]
수빈이가 외친 수의 개수가
- 짝수: 2n => n-1번째
- 홀수: 2n+1 => n번째

반으로 나눠서 최대 힙, 최소 힙으로.
짝수(2n개) => 최대 힙(0.."n-1") / 최소 힙(n...2n-1)
홀수(2n+1개) => 최대 힙(0..n-1)/ 최소 힙("n"...2n)

원소가 하나 들어갈 때

<힙 규칙 맞추기> 
(1) 짝수였던 경우
    - 원소 < 최대 힙의 루트
        최대 힙 루트를 최소 힙에 넣어주고,
        원소는 최대 힙으로 넣어주기
    - 최대 힙의 루트 < 원소 < 최소 힙의 루트
        원소는 최소 힙으로 넣어주기(원소 = 최소 힙의 루트)
    - 원소 > 최소 힙의 루트
        원소는 최소 힙으로 넣어주기

(2) 홀수였던 경우
    - 원소 < 최대 힙의 루트
        원소 최대 힙으로 넣어주기
    - 최대 힙의 루트 < 원소 < 최소 힙의 루트
        원소 최대 힙으로 넣어주기(원소=최대 힙의 루트)
    - 원소 > 최소 힙의 루트
        최소 힙 루트를 최대 힙으로 넣어주기
        원소 최소 힙으로 넣어주기

TRY 1: 런타임 에러(nameerror)
    매번 print문으로 출력하게 함(x가 들어올 때마다)
이후 print문 수정해줬더니 잘 됨.

'''
import sys
import heapq

def main():
    N = int(sys.stdin.readline())
    left = []; right = []   # left: 최대 힙, right: 최소 힙
    right.append(int(sys.stdin.readline())) # i=0
    ans = [right[0]]
    for i in range(1, N):
        # i가 지금까지 들어온 원소의 개수 -1개
        x = int(sys.stdin.readline())
        if i%2 == 0:
            # x 들어가기 전 h는 짝수개
            if x < -1*left[0]:
                left_root = -1*heapq.heappop(left)
                heapq.heappush(right, left_root)
                heapq.heappush(left, -1*x)
            else:
                heapq.heappush(right, x)
            ans.append(right[0])
        else:
            # x 들어가기 전 h는 홀수개
            if x < right[0]:
                heapq.heappush(left, -1*x)
            else:
                right_root = heapq.heappop(right)
                heapq.heappush(left, -1*right_root)
                heapq.heappush(right, x)
            ans.append(-1*left[0])

    for a in ans:
        print(a)

main()