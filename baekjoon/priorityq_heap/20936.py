# 우선순위 계산기: 시간 초과.
# 우선순위 큐로 계산
'''
3*4+5-5+7
참고: https://degurii.tistory.com/187

우선순위 큐, 연결 리스트 이용한 문제
독특한데 되게 신기한 문제.

max부터 해결해야 하므로 우선순위 큐에서 "-1" 해주는 것 잊지 말기!
유니온 파인드 개념 숙지하기!
'''

import sys; read = sys.stdin.readline
from queue import PriorityQueue

class Node:
    # TODO 두 수의 연산 결과, 연산자 우선 순위, 왼쪽 피연산자, 오른쪽 피연산자, 그에 따른 비교 함수 정의해야 함.
    def __init__(self, num):
        self.num = num
        self.llink = None
        self.rlink = None

# TODO find front, find back을 따로 정의하는 게 좋음.

def solution(s):
    
    num2blank = str.maketrans(''.join([str(i) for i in range(10)])+'/', ' '*10+'//')
        # eval 쓸 때 / => // 변환해줘야 하기 때문에 마지막 / 첨자가 들어감. 
    tok2blank = str.maketrans('*/+-', ' '*4)

    num_list = s.translate(tok2blank).split()
    tok_list = s.translate(num2blank).split()
    node_list = []
    q = PriorityQueue()

    for i in range(len(num_list)):
        # 노드 리스트 만들어주기
        node_list.append(Node(num_list[i]))
        if i>0:
            node_list[i].llink = node_list[i-1]
            node_list[i].llink.rlink = node_list[i]

        # 우선순위 큐 작업해 주기
        if i<len(num_list)-1:
            
            q.put((-1*eval(num_list[i]+tok_list[i]+num_list[i+1]), (i, i+1)))   
            
        
    head = node_list[0]
    print(num_list, tok_list)
    
    # 프린트
    while(not q.empty()):
        a,b = q.get()
        print(-1*a, b)

    # 우선순위 큐에 넣고 빼고 하기
    

    answer = 0
    return answer

print(solution(read()))