'''
https://programmers.co.kr/learn/courses/30/lessons/77485


rows	columns	queries	result
6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
100	97	[[1,1,100,97]]	[1]

i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.

'''
import sys; read = sys.stdin.readline
import collections
from pprint import pprint


def solution(rows, columns, queries):
    nums = [list(range(i*columns+1, (i+1)*columns+1)) for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x-1, query)
        # queries에 있는 x1, x2, y1, y2는 각 -1해 줘야 함
        # 즉, 문제상 1번째 행 -> 코드상 0번째 햄
        prev = nums[x1][y1]
        
        # i = 0: (x1, y1+1~y2) (y:+1)
        for j in range(y1+1, y2+1):
            print(x1, j)
            temp = nums[x1][j]
            nums[x1][j] = prev
            prev = temp
        
        # i = 1: (x1+1~x2, y2) (x:+1)
        for j in range(x1+1, x2+1):
            print(j, y2)
            temp = nums[j][y2]
            nums[j][y2] = prev
            prev = temp

        # i = 2: (x2, y2-1~y1) (y:-1)
        for j in range(y2-1, y1-1, -1):
            print(x2, j)
            temp = nums[x2][j]
            nums[x2][j] = prev
            prev = temp

        # i = 3: (x2-1~x1, y1) (x:-1)
        for j in range(x2-1, x1-1, -1):
            print(j, y1)
            temp = nums[j][y1]
            nums[j][y1] = prev
            prev = temp

        

    answer = []
    return answer

print(solution(4, 4, [[1,1,4,4]]))