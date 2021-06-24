# 1로 만들기
'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

12 => 4 => 2 => 1

21 => 7 => 6 => 2 => 1


'''
import sys

N = int(sys.stdin.readline())
min_cnt = 1000001

def goDown(n, cnt):
    global min_cnt
    if n == 1:
        min_cnt = min(min_cnt, cnt)
    elif cnt < min_cnt:
        if n % 3 == 0:
            goDown(n//3, cnt+1)
        if n % 2 == 0:
            goDown(n//2, cnt+1)
        goDown(n-1, cnt+1)


goDown(N, 0)
print(min_cnt)