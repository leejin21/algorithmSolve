# 수식 최대화

from collections import deque

def operate(num1, tok, num2):
    if tok == '*':
        return num1 * num2
    elif tok == '+':
        return num1 + num2
    else:
        return num1 - num2

def solution(expression):
    tok_table = str.maketrans('+-*', "   ")
    num_table = str.maketrans("".join([str(i) for i in range(9)]), " "*9)
    # 0-9 => " "
    numbers =list(map(int, expression.translate(tok_table).split()))
    tokens = expression.translate(num_table).split()
    
    
    # 조합 구하는 거 찾아보기(파이썬에 유용한 툴)
    # numbers = list(map(int, expression.split('+-*')))
    # print(numbers, tokens)
    priorities = [['+', '-', '*'], ['+', '*', '-'], ['*', '+', '-'], ['*', '-', '+'], ['-', '+', '*'], ['-', '*', '+']]
    ans_list = []
    for p in priorities:
        # print(p)
        nums = deque(numbers); toks = deque(tokens)
        p = deque(p)
        answer = 0
        while(toks):
            t = p.popleft()
            rot_cnts = 0
            # 우선순위에 의해 rot_cnts 설정
            while(t in toks):
                num1 = nums.popleft()
                cur_tok = toks.popleft()
                
                if cur_tok == t:
                    num2 = nums.popleft()
                    nums.appendleft(operate(num1, cur_tok, num2))
                    nums.rotate(rot_cnts)
                    toks.rotate(rot_cnts)
                else:
                    nums.append(num1)
                    toks.append(cur_tok)
                    rot_cnts += 1
        ans_list.append(abs(nums[0]))

    # print(max(ans_list))
    

    return max(ans_list)


solution("100-200*300-500+20")
solution("50*6-3*2")