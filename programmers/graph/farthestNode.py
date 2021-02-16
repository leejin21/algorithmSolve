'''
PROBLEM

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

[제한사항]
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

'''

'''
ANSWER

bfs로.
마지막에 최대 값 가지는 간선의 인덱스 찾고, 해당 인덱스와 동일한 값 가지는 노드 개수 세기.

'''
# * MY SOLUTION
from queue import deque

class Node:
    def __init__(self, i):
        self.num = i
        self.link = []
        # self.marked = False

def solution(n, vertex):
    answer = 0

    # * 초기 설정
    nodelist = [Node(i+1) for i in range(n)]
    for v in vertex:
        n1 = nodelist[v[0]-1]; n2 = nodelist[v[1]-1]
        n1.link.append(n2); n2.link.append(n1)
    
    # * dfs
    answer = bfs(nodelist[0], n)

    return answer

def bfs(root, n):
    # dist는 각 노드당 건너가는 그래프의 간선 수
    # CNT는 MAX 간선 수만큼 1번 노드에서 떨어진 노드의 수
    MAX = 0; dist = [0]*n
    q = deque()
    q.append(root)
    
    while(len(q)!=0):
        cur = q.popleft()
        # ! deque.pop()을 호출하면 deque가 스택처럼 동작(선입후출): 테스트2, 테스트6만 통과하고 나머지는 통과 못함.
        for v in cur.link:
            if dist[v.num-1] == 0 and v.num != 1:
                # 아직 방문하지 않았고, 1번 노드 아닌 경우(사이클 생김)
                dist[v.num-1] = dist[cur.num-1]+1
                MAX = max(dist[v.num-1], MAX)
                # print(v.num, dist, MAX)
                q.append(v)

    return dist.count(MAX)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


# * OTHERS SOLUTION
# 출처: https://donis-note.medium.com/프로그래머스-가장-먼-노드-level-3-python-풀이-248455cfa49d

'''
https://www.daleseo.com/python-collections-defaultdict/
collections 에서 defaultdict 설명
: defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘겨주면, 모든 키에 대해 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출해 그 결과값으로 설정해줌.
'''