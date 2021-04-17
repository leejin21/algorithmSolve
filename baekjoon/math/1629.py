# 곱셈
'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

SOLUTION

TRY 1: pow 이용, 2%까지 갔다가 시간초과.
분할정복을 이용한 문제
A % C

TRY 2: 분할정복 이용, 시간 초과. TRY 1과 같은 풀이인 듯.

TRY 3: 

left_remain = right_remain * a 이므로 right_remain을 재귀로 구했으면 left_remain도 자연스럽게 구할 수 있음.

TRY 4:
그런데 홀수면: left_remain = right_remain*a 가 적용(left_remain = a^(b//2+1))
짝수면: left_remain = right_remain*a 가 적용(right_remain = a^(b//2))
'''

import sys; read = sys.stdin.readline

A, B, C = tuple(map(int, read()[:-1].split(" ")))

def findRemain(a, b):
    # 종결조건
    if (b==1):
        return a%C
    else:
        right_remain = findRemain(a, b//2); left_remain = right_remain*a if b%2 == 1 else right_remain
        return (left_remain*right_remain)%C

print(findRemain(A%C, B))