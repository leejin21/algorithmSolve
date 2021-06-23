# 최대공약수와 최소공배수
'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 최대공약수 구하기

일단 각자를 서로소 제곱의 곱으로 구성해 주기
예: A^a1*B^b1*C, A^a2*B^b2 (a1<b1)

=> 최대공약수(교집합)
: A^a1*B^b1

=> 최소공배수(합집합)
: A^a2*B^b2*C

'''

import sys; read = sys.stdin.readline
from collections import defaultdict
from math import sqrt

dd = [defaultdict(int), defaultdict(int)]
n1, n2 = list(map(int, read()[:-1].split(" ")))


def getParts(n, what):
    a = n; i = 2
    while(i<=n and a > 1):
        if a % i == 0:
            dd[what][i] += 1
            a //= i
        else:
            i += 1

    if len(dd[what].keys()) == 0:
        # for 소수
        dd[what][n] = 1

getParts(n1, 0); getParts(n2, 1)
# print(dd)

gcf = 1; lcm = 1
A = set(dd[0].keys()); B= set(dd[1].keys())
# 최대공약수 gcf 구하기
for k in A&B:
    gcf *= pow(k, min(dd[0][k], dd[1][k]))
# 최소공배수 lcm
for k in A|B:
    lcm *= pow(k, max(dd[0][k], dd[1][k]))

print(gcf)
print(lcm)
