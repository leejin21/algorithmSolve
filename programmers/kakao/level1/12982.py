# 예산

def solution(d, budget):
    answer = 0; max_b = 0
    d.sort()
    while(max_b <= budget):
        if answer > len(d) -1: answer += 1; break
        max_b += d[answer]
        answer += 1
    return answer - 1

print(solution([1,3,2,5,4], 3))
print(solution([2,2,3,3], 9))
