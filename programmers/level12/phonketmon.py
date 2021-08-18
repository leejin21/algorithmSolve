# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845
'''
N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법
이떄 같은 종류의 포켓몬을 선택하는 경우 1번으로 취급함.
중복조합인데 이제 제한조건을 곁들인...

종류의 개수로 카운트.
=> 종류의 개수 < len(nums)//2 인 경우
종류의 개수 return
'''
from collections import defaultdict

def solution(nums):
    answer = len(nums)//2
    dd = defaultdict(int)
    
    for n in nums:
        dd[n] += 1
    
    answer  = len(dd) if len(dd) < answer else answer
    
    return answer

print(solution([3,3,3,2,2,2]))