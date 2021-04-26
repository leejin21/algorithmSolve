# 소수 만들기
from math import sqrt

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                answer += 1 if isPrimeNum(nums[i]+nums[j]+nums[k]) else 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer

def isPrimeNum(num):
    if num == 1: return False

    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False

    return True

print(solution([1,2,7,6,4]))


def solution2(nums):
    # 다른 사람 풀이
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer