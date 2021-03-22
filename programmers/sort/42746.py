'''
문제 설명

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
[1, 10, 5, 8] "85110"

solution

try 1
우선순위 큐 이용: max heap, 넣을 때 - 붙여서 넣어 주기
우선순위는 4개로, 예를 들어 9 => 0009 이렇게.(제한사항에 맞춤.)

try 2
우선순위 큐를 이용하는 게 아니었음. 우선순위 큐를 이용하면 34와 3 중 3을 먼저 선택하기 때문에 탈락.
[파이썬 알고리즘 인터뷰]에 사실 동일한 문제가 있어서 공부도 했었는데 이렇게 틀림.. 반성하자 이진...


1 10 5 8
1 => 110 => 5110

'''

import heapq
from functools import reduce, cmp_to_key


def try1(numbers):
    heap = []; ans = ''
    for n in numbers:
        heapq.heappush(heap, tuple(map(lambda x: int(x)*-1, str(n))))
    
    while (heap):
        x = list(map(lambda i: str(i*-1), heapq.heappop(heap)))
        ans += reduce(lambda i, j: i+j, x)
        
    return str(int(ans))


def try2(numbers):
    # 삽입 정렬 구현: 시간 초과
    def needSwap(x, y):
        # print(str(x)+str(y), str(y)+str(x))
        return str(x) + str(y) > str(y) + str(x)
    for i in range(1, len(numbers)):
        # numbers[i]
        j = i
        while(j>0 and needSwap(numbers[j], numbers[j-1])):
            # numbers[i]가 움직이는 애, numbers[j]와 비교하기
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j-=1

    return str(int(reduce(lambda x, y: str(x)+str(y), numbers)))

def solution(numbers):
    ans = [str(i) for i in numbers]
    def comparator(x, y):
        # t1 > t2인 경우 1 반환, t1 < t2인 경우 -1 반환, t1 = t2인 경우 0 반환
        t1 = x+y; t2 = y+x
        return (int(t1)>int(t2)) - (int(t1)<int(t2))
    return str(int(''.join(sorted(ans, key=cmp_to_key(comparator), reverse=True))))
    

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1, 10, 5, 8]))


# getNum(-1,-12,-3)