
import sys; read = sys.stdin.readline

def solution(numbers):
    N = sum(range(10))
    nsum = sum(numbers)
    return N - nsum

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))