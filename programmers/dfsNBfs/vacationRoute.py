# https://programmers.co.kr/learn/courses/30/lessons/43164
# 프로그래머스 여행경로
'''
PROBLEM

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

[제한사항]
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 ^알파벳 순서가 앞서는 경로^를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''

'''
SOLUTION

==1번 시도==
DAG가 아님.. 사이클 존재함.
따라서 그냥 방향 그래프대로 풀면 될 듯.

dictionary time complexity
https://wiki.python.org/moin/TimeComplexity

==2번 시도==
설마설마했는데 같은 내용의 티켓이 있는 반례가 있었다.
https://programmers.co.kr/questions/15603

tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]
answer = ['ICN', 'A', 'ICN', 'A', 'C']
'''
from collections import defaultdict

graph = defaultdict(dict)
# (예) graph = defaultdict(<class 'dict'>, {'ICN': {'A': 2}, 'A': {'ICN': 1, 'C': 1}})

answer = []

def solution(tickets):
    global graph
    getGraph(tickets)
    dfs('ICN')
    answer.reverse()
    return answer

def dfs(ap):
    # * graph에 담긴 ticket들 알파벳 순으로 소모하기
    global graph
    for dest in sorted(graph[ap]):
        if graph[ap][dest] > 0:
            # 방문 시 티켓 소모, 스택에 넣어두기
            graph[ap][dest] -= 1
            dfs(dest)
    # dfs, 가장 깊은 노드부터 기록 -> solution에서 reverse해 줌
    answer.append(ap)

def getGraph(tickets):
    # * graph에 tickets 정보 저장
    # O(len(tickets))
    global graph
    for a1, a2 in tickets:
        try:
            if graph[a1][a2] > 0:
                # ! 2번 시도 반례 고려
                # 반례 = 출발도착이 같은 티켓이 2개 이상 있는 경우: graph에 방향과 해당 내용의 티켓 수 정보 저장.
                graph[a1][a2] += 1
        except:
            graph[a1][a2] = 1

# tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]
# solution(tickets)
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
# print(graph)
# print(visited)