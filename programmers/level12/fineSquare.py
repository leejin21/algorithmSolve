# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd


def solution(w,h):
    answer = 1
    # GCD = gcd(w, h)
    cnt = 0
    tot_x = max(w, h)
    tot_y = min(w, h)
    if tot_x == tot_y:
        return w*h - w
    # print(tot_x, tot_y, GCD)
    # incli_x = tot_x // GCD
    # incli_y = tot_y // GCD
    incli_x = tot_x
    incli_y = tot_y
    incli = incli_y/ incli_x

    pre_y = 0
    # cnt_list = [[0]*incli_x for i in range(incli_y)]
    for x in range(1, incli_x+1):
        y = x * incli
        # print(x, y, pre_y)
        if y-int(y) == 0:
            cnt += 1
            break

        elif int(y) == int(pre_y):
            # 아직 y를 못 넘겼거나, 마지막(x=incli_x) == y가 정수일 경우
            cnt +=1
            
        else:
            # y를 넘긴 경우.
            cnt += 2
            pre_y = y
        # print("cnt", cnt)
    # print(cnt_list)
    return w*h - cnt*(tot_x//x)



print(solution(8, 12))

print(solution(5, 2))