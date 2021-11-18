# 이중 우선순위 큐
# https://programmers.co.kr/learn/courses/30/lessons/42628
'''
["I 7","I 5","I -5","D -1"]
<교훈>
1. 아이패드 제대로 활용하기. 
쓰여 있는 예제의 변형 케이스들(간단하면서 반례인 것들) 자세하게 neat하게 분석해 놓기
-> 그래야 디버깅 때 쉬움.
2. 상세 알고리즘은 어차피 쓸 거니까, 용어 위주로 숫자 태그하면서 적어두기
'''
from collections import defaultdict
import heapq

def solution(operations):
    answer = []
    maxHeap = []; minHeap = []
    d = defaultdict(int)
    def deleteValue(heap, param, isLast=False):
        VAL = heapq.heappop(heap)*param
        while(d[VAL]==0 and heap):
            # 진짜 최솟값 삭제할 때까지 시체 처리
            VAL = heapq.heappop(heap)*param
        # print(heap, d)
        if not isLast: d[VAL] -= 1
        cnt = heap.count(VAL) - d[VAL] - 1
        while(cnt>0):
            VAL = heapq.heappop(heap)*param
            cnt -= 1
        return VAL

    for cmd in operations:
        op, num = cmd.split(" ")
        num = int(num)
        if op == 'I':
            d[num] += 1
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, -1*num)
        elif op == 'D' and num == -1 and minHeap:
            # 최솟값 삭제
            print(deleteValue(minHeap, 1))
        elif op == 'D' and num == 1 and maxHeap:
            # 최댓값 삭제
            print(deleteValue(maxHeap, -1))
    if minHeap and maxHeap:
        answer.append(deleteValue(maxHeap, -1, True))
        answer.append(deleteValue(minHeap, 1, True))
    else:
        answer = [0,0]
    # answer = [heapq.heappop(maxHeap)*-1, heapq.heappop(minHeap)]
    return answer

# print(solution(["I 7","I 5","I -5","D -1"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333", "D -1", "D -1"]))