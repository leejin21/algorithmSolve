# 순위

'''
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2

4, 3 => 4
4, 2 => 4
3, 2 => 3
1, 2 => 1
2, 5 => 2

2 이후
4 - 3, 2

3 이후
4 - 3
3 - 2

4 이후
4 - 3
3 - 1
1 - 2

5 이후
4 - 3
3 - 1
1 - 2
2 - 5

결과를 어떻게 하면 명확하다고 할 수 있을까?
규칙이 어떻게 되는가?


가면서 세고 오면서 세기: tot >= N-1인 경우 체크.

문제는 어떻게 해야, 중복되지 않게 셀 수 있을 지임.

'''
from collections import defaultdict
import sys

sys.setrecursionlimit(20000)
node_locations = []

class Node:
    def __init__(self, num):
        self.num = num
        self.parent = []
        self.visit = False


def solution(n, results):
    global node_locations
    answer = 0
    node_list =[None]+[Node(i) for i in range(1, n+1)]
        # node_list[1] = Node(1)
    node_locations = [[0,0] for i in range(n+1)]
    # print(node_locations)
    for res in results:
        nwin, nlos = res
        winner = node_list[nwin]; loser = node_list[nlos]
        for pnode in loser.parent:
            if needCutNode(pnode.num, winner):
                print("remove", loser.num, pnode.num)
                loser.parent.remove(pnode)
        loser.parent.append(winner)

    for ni in range(1, len(node_list)):
        if not node_list[ni].visit:
            recursion(node_list[ni], 0)

    for loc in node_locations:
        print(loc)
        if n-1 <= sum(loc):
            answer += 1
    return answer

def needCutNode(target_num, node):
    # 기존 loser.parent 중 노드랑 겹치는 거 있으면 loser.parent에서 삭제하기: return True, False
    if node.parent:
        for pnode in node.parent:
            if pnode.num == target_num:
                return True
            if needCutNode(target_num, pnode): return True
    return False


def recursion(node, level):
    cnt = 0
    node.visit = True
    node_locations[node.num][0] += level
    print(node.num, node_locations)
    if node.parent:
        print(node.num, end=" ")
        for nnode in node.parent:
            print(nnode.num, end = " ")
        print()
        for nnode in node.parent:
            recursion(nnode, level+1)
            cnt += node_locations[nnode.num][1]
        node_locations[node.num][1] = cnt + 1
    else:
        node_locations[node.num][1]= 0

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [6, 7], [6, 8]]))