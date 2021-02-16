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

의존성 그래프, DAG
: DAG인 이유 => 방향 그래프, 사이클이 없음.

dfs로 위상 정렬

********************************************
DAG가 아님.. 사이클 존재함.
따라서 그냥 방향 그래프대로 풀면 될 듯.


dictionary time complexity
https://wiki.python.org/moin/TimeComplexity
'''

graph = dict(); visited = dict()
answer = []

def solution(tickets):
    global answer
    # * adjacent list 만들기
    getSortedAirports(tickets)
    
    dfs('ICN')

    # for ap in sorted(graph.keys()):
    #     if not visited[ap]:
    #         dfs(ap)

    answer.reverse()
    return answer

def dfs(ap):
    visited[ap] = True
    for dest in sorted(graph[ap]):
        if not visited[dest]:
            dfs(dest)
    answer.append(ap)


def getSortedAirports(tickets):
    # tickets에서 알파벳 순서대로 찾기, 딕셔너리로.
    # O(2*len(tickets) + nlogn)
    # airports = []; graph = []
    global graph, visited
    # 각 1D 리스트, 2D 리스트
    for tl in tickets:
        # print(tl[0], tl[1])

        if tl[0] in graph.keys():
            # 이미 추가한 stt 노드인 경우
            graph[tl[0]].append(tl[1])
            
        else:
            # 처음 보는 stt 노드인 경우
            graph[tl[0]] = [tl[1]]
            visited[tl[0]] = False
        
        if tl[1] not in graph.keys():
            # dest 노드 추가해주기
            graph[tl[1]] = []
            visited[tl[1]] = False


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(graph)
print(visited)