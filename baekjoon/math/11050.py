'''
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 NCK를 구하는 프로그램을 작성하시오.

NCK = (N)(N-1)...(N-K+1)/(1)(2)...(K)

'''
import sys
N, K = list(map(int, sys.stdin.readline().split(" ")))
tot = 1

for n in range(N, N-K, -1):
    tot *= n

for k in range(2, K+1):
    tot = tot // k

print(tot)