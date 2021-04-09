# 소수 찾기
'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

4
1 3 5 7

출력
주어진 수들 중 소수의 개수를 출력한다.

3

소수 구할 때 주의사항
* 정수(루트 n)보다 작거나 같고, 1보다 큰 수들로 나누어 떨어지는 지 확인해야 함
* 1은 소수가 아님.

추가사항
* sqrt는 math 라이브러리 안에서 import해야 함(내장 함수가 아님.)

'''

# 1은 소수가 아님.

import sys
from math import sqrt

N = int(sys.stdin.readline())
natnums = list(map(lambda i: int(i), sys.stdin.readline().split(" ")))
cnt = 0; prime = True

for n in natnums:
    prime = True
    if n == 1:
        prime = False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: # 소수가 아님
            prime = False
            break
    if prime:
        cnt += 1

print(cnt)