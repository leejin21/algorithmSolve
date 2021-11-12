# [3차] n진수 게임
'''
https://programmers.co.kr/learn/courses/30/lessons/17687

n진법에 대한 숫자의 모음을 문자열로 나타내고 이걸 슬라이싱함
정답 => 문자열[p-1:t*m:m]

몇번째에 끊어야 하는 걸까?

0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1
V     V     V     V
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4
   V           V           V           V
p = 2, m = 4, t = 3

'''
import collections
import string

tmp = string.digits+string.ascii_uppercase
# tmp는 '012...9'+'ABCD...XYZ'
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    i = 0
    while(len(answer)<t*m+1):
        answer += convert(i, n)
        # print(answer)
        i += 1
    return answer[p-1:t*m:m]

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))