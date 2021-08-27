# 우선순위 계산기: 시간 초과.

'''
3*4+5-5+7

'''


import sys; read = sys.stdin.readline
from collections import deque

def operate(x, t, y):
    if t == '*':
        return x * y
    elif t == '/':
        return x // y
    elif t == '+':
        return x + y
    else:
        # t == '-'
        return x - y


def solution(S):
    TOK_DICT = {'*': 1, '/': 1, '+': 0, '-': 0}

    tok2blank = str.maketrans('*/+-', '    ')
    num_list = list(map(int, S.translate(tok2blank).split()))

    num2blank = str.maketrans(''.join([str(i) for i in range(10)]), ' '*10)
    # 0-9 -> 0*10
    tok_list = S.translate(num2blank).split()

    # print(num_list)
    # print(tok_list)

    tok_q = deque(tok_list)
    num_q = deque(num_list)

    while(tok_q):
        MAX_TOK_PR = -1; MAX_VAL = 0; MAX_I = -1
        # 먼저 num_q, tok_q로 가장 큰 값을 가지는 i 선택해서 연산하기
        for i in range(len(num_q)-2, -1, -1):
            val = operate(num_q[i], tok_q[i], num_q[i+1])
            if val > MAX_VAL:
                MAX_I = i
                MAX_TOK_PR = TOK_DICT[tok_q[i]]
                MAX_VAL = val
            elif val == MAX_VAL:
                if TOK_DICT[tok_q[i]] > MAX_TOK_PR:
                    MAX_I = i
                elif TOK_DICT[tok_q[i]] ==  MAX_TOK_PR:
                    MAX_I = min(i, MAX_I)
                    # 더 작은 i 값으로 해 주기
        # tok_q, num_q 반영하기
        ROT_CNT = 0 # 원상태 복귀 위해

        # 큐에서 -i만큼 rotate해서 pop 
        tok_q.rotate(-1*MAX_I)
        t = tok_q.popleft()

        num_q.rotate(-1*MAX_I)
        x = num_q.popleft()
        y = num_q.popleft()

        # if MAX_VAL != operate(x, t, y):
        #     print("ERROR")
        num_q.appendleft(MAX_VAL)

        # 원상태 복귀하기
        num_q.rotate(MAX_I)
        tok_q.rotate(MAX_I)
    
    return num_q[0]

print(solution(read()))