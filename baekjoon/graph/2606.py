# 바이러스
import sys; read = sys.stdin.readline


class Node:
    def __init__(self, num):
        self.num = num
        self.visit = False
        self.links = []

def dfs(node):
    global virus_cnt
    if node and not node.visit:
        node.visit = True
        virus_cnt += 1
        for next_node in node.links:
            dfs(next_node)

N = int(read())
E = int(read())

node_list = [None]+[Node(i) for i in range(1, N+1)]
virus_cnt = 0
for _e in range(E):
    n1, n2 = list(map(int, read()[:-1].split(" ")))
    node_list[n1].links.append(node_list[n2])
    node_list[n2].links.append(node_list[n1])

dfs(node_list[1])
print(virus_cnt-1)
    # 1번 컴퓨터 cnt에서 제외
