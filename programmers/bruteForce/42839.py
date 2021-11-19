# 소수 찾기
# 완전 탐색

'''
일단 순열로 찾고, 그거 붙여서 소수인 지 검사하기
'''
import math
import itertools, collections

def solution(numbers):
    answer = 0
    confirmed_Nums = collections.defaultdict(lambda: None)
    def isPrimeNum(n):
        
        if n == 0 or n == 1: 
            confirmed_Nums[n] = False
            return
        for i in range(2, math.floor(math.sqrt(n))+1):
            # print(i)
            if n % i == 0:
                confirmed_Nums[n] = False
                return
        confirmed_Nums[n] = True
        return

    for i in range(1, len(numbers)+1):
        for num_it in list(itertools.permutations(numbers, i)):
            # 중복이 틀림
            n = int(''.join(num_it))
            if not confirmed_Nums[n]:
                isPrimeNum(n)
                answer += 1 if confirmed_Nums[n] else 0
    return answer

# print(solution('143'))
# print(solution('17'))
print(solution('011'))