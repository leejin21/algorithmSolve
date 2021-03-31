# -*- coding: utf-8 -*-
# 감소하는 수
'''
문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.

n>=2에 대해
S(n,1) = 1
S(n,2) = 1 + S(n-1,1)
...
S(n,k) = 1 + S(n-1, k-1)
이때 S(n,k)는 10^(n-1)의 자릿수를 가지고 k = 10^(n-1)번째 자리의 숫자인, 감소하는 수의 개수
    예) S(3,2) = 1 + S(2,1)이고 구성 감소수는 {200, 210}임.

S(n,k).sum(n=0,k=0부터 n=a,k=b)가 N보다 작고 최댓값을 가진다고 할때

TRY 2:
반례: 9876543210000000
따라서 0이 두개 이상 return하면 안됨.

100도 안됨.

"굳이 어려운 길로 가지 말자.. 제발..."

다시 풀기....

'''
import sys
from collections import deque
memo = []; N = 0; cnt = 9
ans = deque(); noAns = False

def main():
    global memo, N, cnt
    N = int(sys.stdin.readline())
    if N <= 9:
        print(N); return
    memo += [0]*10, [1]*10, [0]*10,
    digit = 2; front = 1; cnt =9
    last = (0, 0, 0)       # dummy init

    while(cnt < N):
        last = (digit, front, cnt)
        memo[digit][front] = getDescCnts(digit, front)
        
        cnt += memo[digit][front]
        if front == 9:
            memo += [0]*10,
            # memo[아무][0] = 1: 나중에 가지 칠 때 000인 부분도 있을 것이므로
            digit += 1; front = 1
        else:
            front += 1

    if cnt == N:
        while(digit>0):
            ans.append(front-1)
            front -= 1; digit -= 1
    else:
        last_digit, last_front, cnt = last
        findDescNum(last_digit, last_front)
    print(memo)
    print(int(''.join(map(str, ans))))
    

def findDescNum(digit, front):
    global cnt, noAns
    if cnt == N:
        if digit == 2:
            ans.appendleft(0)
        elif digit > 2:
            ans.clear()
            noAns = True
        else:
            ans.appendleft(front)
    else:
        temp = cnt
        for k in range(front):
            pre_temp = temp
            temp += getDescCnts(digit-1, k)
            if temp >= N:
                cnt = temp if temp==N else pre_temp
                findDescNum(digit-1, k)
                if not noAns:
                    ans.appendleft(front)
                break

def getDescCnts(digit,front):
    # S(digit, k) = 1+ S(digit,1) + ... + S(digit, k-1)
    if digit == 1:
        return 1
    cnt = 0
    for k in range(front):
        cnt += memo[digit-1][k]
    return cnt
    
main()