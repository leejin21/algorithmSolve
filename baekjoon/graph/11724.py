# 11724. 연결 요소의 개수

import sys; read = sys.stdin.readline
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, num):
        self.num = num
        self.connect = []
        self.visit = False
    
    def add2Conn(self, node):
        self.connect.append(node)

def visitGraph(node):
    node.visit = True
    for next_node in node.connect:
        if not next_node.visit:
            visitGraph(next_node)


N, M = list(map(int, read()[:-1].split(" ")))

nodelist = [None]+[Node(i) for i in range(1, N+1)]
for _ in range(M):
    n1, n2 = list(map(int, read()[:-1].split(" ")))
    nodelist[n1].add2Conn(nodelist[n2])
    nodelist[n2].add2Conn(nodelist[n1])

# 방문하기
cnt = 0
for node in nodelist[1:]:
    if not node.visit:
        cnt += 1
        visitGraph(node)
        
print(cnt)