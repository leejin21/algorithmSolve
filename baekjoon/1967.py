# TreeDiameter.py
# 백준 1967번 트리의 지름
'''
PROBLEM

트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 "하나만" 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다(가장 끝과 끝에 존재하는 노드들). 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 "트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이"를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.
트리의 노드는 1부터 n까지 번호가 매겨져 있다.

노드의 개수 ~10000개
메모리 제한 128MB
'''

'''
SOLUTION

(실패 1)
1. 노드의 갈래마다 해당 노드를 포함했을 때의 최대 지름을 구하고
2. 1을 이용해서 양 갈래마다 해당 노드를 포함한 최대 지름을 구함
3. 2 중 최대값을 찾아서 도출

=> 왜 실패했는 지 모르겠음.

(답지)
부모, 자식간의 관계를 가지는 '트리'가 아니라 '그래프'로 봐야 함.
1. 그래프의 노드 중 하나를 골라서 해당 노드와 가장 떨어져 있는 노드(end node)를 구함.
    -> 어떤 노드와 가장 멀리 떨어져 있는 노드는 지름 양 끝의 노드이다
    (가중치가 5이면 노드가 4개 그 사이에 끼어져 있다고 치면 됨.)
2. end node에서 가장 떨어져 있는 노드와의 거리를 구함
3. 1,2 과정은 dfs(전위 || 중위 || 후위)로 이루어진다.

<DFS>
루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
트리에서는 전위, 중위, 후위 순회 방법이 있다.

(실패 2)
dfs를 재귀 함수로 구현하면 RecursionError로 추정되는 런타임에러가 뜸.

(성공)
dfs를 for문으로 구현
'''
# from functools import reduce

# 글로벌 변수
MAX = -1
END_NODE = None

class Node:
    def __init__(self, num):
        self.num = num
        self.visit = False
        self.links = []
        # links = [[node, edge], [node, edge]]

def main():
    global MAX, END_NODE
    # * INITIALIZATION CODE
    N = int(input())
    nodeList = [Node(i) for i in range(1, N+1)]
        # N + 1개가 맞음.
    saveInput(N, nodeList)
    
    # * MAIN CODE
    # 1. 임의의 한 노드에서 가장 먼 노드 찾기(=endnode)
    # getEndpoint(nodeList[0], 0)
    forGetEndPoint(nodeList[0])
    # 2. max, visit 초기화시켜주기
    MAX = -1
    for n in nodeList:
        n.visit = False
    # 3. endnode에서 가장 먼 노드와의 거리 찾기
    # getEndpoint(END_NODE, 0)
    forGetEndPoint(END_NODE)
    print(MAX)

def forGetEndPoint(node):
    # 재귀가 stack 이용하는 거라서 그 개념 차용
    global MAX, END_NODE
    stack = []; d = 0
    stack.append([node, d])
    while(len(stack) != 0):
        cur, d = stack.pop()
        cur.visit = True
        if (d > MAX):
            MAX = d
            END_NODE = cur
        for l in cur.links:
            n, e = l
            if not n.visit: stack.append([n, d+e])
    
# !재귀함수로 하면 실패
def getEndpoint(node, d):
    # 재귀 함수, visit한 데 아닌 데만 visit해 주기
    global MAX, END_NODE
    node.visit = True
    if (d>MAX): 
        MAX = d
        END_NODE = node
    for l in node.links:
        n, e = l
        if not n.visit: getEndpoint(n, d+e)

def saveInput(N, nodeList):
    for _ in range(N-1):
        # nodeList에 다 정리해서 넣어주기
        parent, child, edge = (int(i) for i in input().split())
        pnode = nodeList[parent-1]; cnode = nodeList[child-1]
        
        pnode.links.append([cnode, edge])
        cnode.links.append([pnode, edge])
        
main()