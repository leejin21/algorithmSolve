# 입국심사
# 프로그래머스 이분탐색
'''
이게 왜 이분탐색? 이라는 생각이 들지만
n=6, times=[7, 10]

MAX = 60
1, 6*10

[반례가 있음]

'''
import sys; read = sys.stdin.readline
import collections

sys.setrecursionlimit(10000)

def solution(n, times):
    answer = 0
    left = 0; right = max(times)*n
    # print(left, right)
    while left < right:
        med = left + (right-left)//2
        val = 0
        for t in times:
            val+= med//t
        if val >= n:
            right = med
        else:
            left = med + 1
    answer = left
    return answer

print(solution(6, [7,10]))