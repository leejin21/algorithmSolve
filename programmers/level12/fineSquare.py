# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048



'''
정답
https://taesan94.tistory.com/55

생각해 보면 직사각형에서 대각선으로 갈 때
무조건 가로로 w만큼, 그리고 세로로 h만큼 간다.
그런데 가로로 갈때 따로, 세로로 갈 때 따로 간다고 생각하면 1개의 정사각형에서 출발하기 떄문에 -1을 해줘야 한다.
따라서 w+h-1만큼의 사각형을 거쳐 간다.

'''

from math import gcd


def solution(w,h):
    answer = 1
    GCD = gcd(w, h)
    cnt = 0
    
    incli_x = w // GCD
    incli_y = h // GCD

    pre_y = 0
    
    # print(cnt_list)
    return w*h - (incli_x + incli_y -1)*GCD



print(solution(8, 12))
print(solution(5, 2))