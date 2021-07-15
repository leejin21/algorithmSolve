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


가면서 세고 오면서 세기



'''
from collections import defaultdict

class Node:
    def __init__(self, num):
        self.num = num
        self.child = []

def solution(n, results):
    answer = 0
    node_list =[None]+[Node(i) for i in range(1, n+1)]
    crash_dict = defaultdict(list)
        # node_list[1] = Node(1)
    for res in results:
        nwin, nlos = res
        winner = node_list[nwin]; loser = node_list[nlos]
        if winner.child:
            crash_dict[nwin].append(nlos)
            winner.child.append(loser)
        else:
            for key, val in crash_dict.items():
                if nwin in val and nlos in val:
                    
            winner.child.append(loser)
    return answer