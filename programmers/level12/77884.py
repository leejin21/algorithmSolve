# 약수의 개수와 덧셈
'''
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.


[약수 구하기]
N을 k = 2부터 루트N까지 나눴을 때
N % k == 0 인 경우 k와 N//k를 집합에 추가.
집합의 길이 구하면 약수의 개수 나옴.

'''
import sys, math

def solution(left, right):
    answer = 0
    for N in range(left, right+1):
        s = set()
        for k in range(1, math.floor(math.sqrt(N))+1):
            if N % k == 0:
                s.add(k); s.add(N//k)
        answer = (answer + N) if len(s) % 2 == 0 else (answer - N)
        print(answer, N, s)

    return answer

print(solution(13, 17))
print(solution(24, 27))