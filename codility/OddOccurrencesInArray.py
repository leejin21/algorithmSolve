
from collections import defaultdict
def solution(A):
    # write your code in Python 3.6
    d = defaultdict(int)
    for a in A:
        if d[a] == 1:
            # 짝 맞춰줌
            d[a] = 0
        else:
            d[a] += 1
    
    return [k for k, v in d.items() if v == 1][0]

    
print(solution([9,2,9,2,1,1,1,1, 9]))