'''
PROBLEM
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
'''

'''
SOLUTION
계속 dfs로 해왔으니까 bfs로 해보기!
visit 배열 만들기, queue 배열 만들기
dfs로 진행(bfs랑의 차이점?)


list comprehension, filter and lambda
https://3months.tistory.com/338
'''
# * Queue 이용: list와 달리 get이 O(1)의 연산을 가짐
# 단 Queue에서 데이터 접근은 O(n)임
from queue import Queue

def solution(n, computers):
    # 노드 번호는 0번부터 세기
    visit = [False]*n; que = Queue(); unvnode_list = [i for i in range(n)]
    # 차례로 인덱스=노드번호: visit bool, 해당 그래프에서 bfs 도는 큐, unvisited node list
    que.put(0); net_cnt = 1
    while(True):
        cur = que.get(); visit[cur] = True
        # print(cur, visit, unvnode_list, net_cnt)
        for i,v in enumerate(computers[cur]):
            if v == 1 and i!=cur and not visit[i]:
                que.put(i)

        # 이번에 visit한 unvnode_list 요소에서 삭제
        for i, v in enumerate(unvnode_list):
            if visit[v] == True:
                del unvnode_list[i]

        # 네트워크 하나 더 있을 때: 큐에 다시 넣어서 인접 노드에 대한 visit 다 True로
        if que.qsize() == 0 and len(unvnode_list)!=0:
            net_cnt += 1
            que.put(unvnode_list.pop())
        # 모든 노드 다 방문했을 때
        elif len(unvnode_list)==0:
            break

    return net_cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 2

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# 1