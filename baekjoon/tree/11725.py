# 트리의 부모 찾기

'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

7
1 6
6 3
3 5
4 1
2 4
4 7

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

4
6
1
3
1
4

'''

import sys; read = sys.stdin.readline
from collections import defaultdict

class Node:
    def __init__(self, num):
        self.num = num
        self.down_link = defaultdict(returnFalse)
        
def returnFalse():
    return False

def addLink(x, y):
    node_list[x-1].down_link[y] = True
    node_list[y-1].down_link[x] = True    

def removeLinks(pre_node, node):
    node.down_link[pre_node.num] = False
    for dn, dnisreal in node.down_link.items():
        if dnisreal:
            parent_list[dn] = node.num
            removeLinks(node, node_list[dn-1])

sys.setrecursionlimit(10000000)
N = int(read())
node_list = [Node(i) for i in range(1, N+1)]
parent_list = [0]*(N+1)

links = []
for _ in range(N-1):
    x, y = list(map(int, read()[:-1].split()))
    addLink(x,y)

removeLinks(Node(-1), node_list[0])
for i in range(2, len(parent_list)):
    print(parent_list[i])

# for node in node_list:
#     print(node.num)
#     print(node.down_link)
