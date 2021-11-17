'''
[LRU 기법: 참조된 지 가장 오래된 페이지가 교체 대상.]

대소문자 구분X

2 0 1 3
[0]
2 1 3 0

[조건 수도 코드로 써가면서 하기.......]
'''
import collections

def solution(cacheSize, cities):
    answer = 0
    queue = collections.deque()
    if len(cities) == 0: return 5
    for city in cities:
        cityLowerCase = city.lower()
        if cityLowerCase in queue:
            print("cache hit")
            # cache hit
            # 이때 스택 대이동
            city_idx = queue.index(cityLowerCase) # 3
            queue = collections.deque(list(queue)[:city_idx]+list(queue)[city_idx+1:]+[cityLowerCase])
            answer += 1
        else:
            print("cache miss")
            # cache miss
            if len(queue) >= cacheSize and cacheSize >0:
                queue.popleft()
            if cacheSize != 0:
                queue.append(cityLowerCase)
            answer += 5
        print(queue, answer)
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(5, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, []))