# 트리의 지름

'''
일단 2차원 리스트 만들어 주기



'''
import sys; read = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.link = []
        self.num = num
        self.visit = False

def getTreeDiam(node):
    global MAXDIA
    node.visit = True
    MAX = 0; SEC_MAX = 0
    for nn in node.link:
        if not nn[0].visit:
            below = nn[1]+getTreeDiam(nn[0])
            if MAX < below:
                SEC_MAX = MAX
                MAX = below
            elif SEC_MAX < below:
                SEC_MAX = below
    MAXDIA = max(MAXDIA, MAX+SEC_MAX)
    # print(node.num, MAX, SEC_MAX, MAXDIA)
    return MAX


N = int(read()); MAXDIA = 0
node_list = [None] + [Node(i) for i in range(1, N+1)]
for i in range(N):
    inp = list(map(int, read()[:-4].split()))
    for j in range(1, len(inp), 2):
        node_list[inp[0]].link.append((node_list[inp[j]], inp[j+1]))

# for node in node_list[1:]:
#     for n in node.link:
#         print(node.num, n[0].num, n[1])


getTreeDiam(node_list[1])
print(MAXDIA)