# 코딜리티

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0 or K == 0:
        return A
    
    if len(A) == K:
        return A
    if len(A) > K:
        # if A가 K보다 큰 경우
        rot = K
    else:
        # if K가 A보다 큰 경우
        rot = K % len(A)
    # print(rot)
    q = deque(A)
    q.rotate(rot)
    return list(q)

# print(solution([3, 8, 9, 7, 6], 3))