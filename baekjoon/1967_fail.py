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

(실패)
1. 노드의 갈래마다 해당 노드를 포함했을 때의 최대 지름을 구하고
parent - child1 - 쭉
        - child2 - 쭉
2. 1을 이용해서 양 갈래마다 해당 노드를 포함한 최대 지름을 구함
3. 2 중 최대값을 찾아서 도출

=> 왜 실패했는 지 모르겠음.









(성공)
부모, 자식간의 관계를 가지는 '트리'가 아니라 '그래프'로 봐야 함.
1. 그래프의 노드 중 하나를 골라서 해당 노드와 가장 떨어져 있는 노드(end node)를 구함.
    -> 어떤 노드와 가장 멀리 떨어져 있는 노드는 지름 양 끝의 노드이다
    (가중치가 5이면 노드가 4개 그 사이에 끼어져 있다고 치면 됨.)
2. end node에서 가장 떨어져 있는 노드와의 거리를 구함
3. 1,2 과정은 dfs(전위 || 중위 || 후위)로 이루어진다.

<DFS>
루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
트리에서는 전위, 중위, 후위 순회 방법이 있다.
'''
from functools import reduce

class Node:
    def __init__(self, num):
        self.num = num
        self.e1 = 0; self.e2 = 0
        self.n1 = None; self.n2 = None

        self.oneD = 0           # 자식 노드 둘 중 한 갈래의 최대 길이
        self.twoD = 0           # 자식 노드 양 갈래 모두 포함한 최대 지름 길이
    
    def childNum(self):
        if (self.n1 and self.n2):
            return 2
        elif (self.n1):
            return 1
        return 0

    def calOneD(self, child_num):
        if (child_num == 2):
            self.oneD = max(self.n1.oneD + self.e1, self.n2.oneD + self.e2)
        elif (child_num == 1):
            self.oneD = self.n1.oneD + self.e1

        return self.oneD
        
    def calTwoD(self, child_num):
        if (child_num == 2):
            self.twoD = self.n1.oneD + self.e1 + self.n2.oneD + self.e2
        elif (child_num == 1):
            self.twoD = self.n1.oneD + self.e1

        return self.twoD

    def printMe(self):
        print(self.num)
        if (self.n1):
            print("|_", self.e1, "__", self.n1.num)
        if (self.n2):
            print("|_", self.e2, "__", self.n2.num)

def main():
    # * INITIALIZATION CODE
    N = int(input())
    nodeList = [None]
    nodeList += [Node(i) for i in range(1, N+1)]
        # N + 1개가 맞음.

    saveInput(N, nodeList)

    # * MAIN CODE
    getDiameter(nodeList[1])
    diameters = [node.twoD for node in nodeList[1:]]
    return reduce(lambda a,b: max(a,b), diameters)
    
    # * CONFIRM CODE
    # print(len(nodeList))
    # for node in nodeList[1:]:
        # print(node.num, node.twoD)
    # print('helloo')

def getDiameter(node):
    # 재귀 함수, 후위 순회 방식
    cn = node.childNum()
    if (cn != 0):
        # print("순서:", node.num)
        # left => right => self
        getDiameter(node.n1)
        if (cn == 2):
            getDiameter(node.n2)
        node.calOneD(cn)
        node.calTwoD(cn)
        # print(node.num, node.oneD, node.twoD)

def saveInput(N, nodeList):
    for _ in range(N-1):
        # nodeList에 다 정리해서 넣어주기
        parent, child, edge = (int(i) for i in input().split())
        pnode = nodeList[parent]; cnode = nodeList[child]
        
        if (pnode.n1):
            pnode.e2 = edge; pnode.n2 = cnode
        else:
            pnode.e1 = edge; pnode.n1 = cnode


print(main())