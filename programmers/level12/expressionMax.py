# 수식 최대화
'''
[교훈]
1. 종이 연습장에 해야 할 일 차근차근 풀어서 쓰기. 내 방식대로 가는 거다.


[기록해 둘 것]
1. 조합 구하는 것 관련 쓸모 있는 거 있는 지 찾아보기
2. eval 함수 찾아보기
3. deque rotate 함수(+, -)

[틀렸던 이유]
1. 런타임 에러가 나올 만한 곳이 tok_table이랑 num_table이었는데 확인해보니까 0-9 -> " "*10인데 0-8로 했더라.
!! range 헷갈리지 말자 !!
'''

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
    num_table = str.maketrans("".join([str(i) for i in range(10)]), " "*10)
    # 0-9 => " "
    numbers =list(map(int, expression.translate(tok_table).split(" ")))
    tokens = expression.translate(num_table).split()
    print(numbers, tokens)
    
    
    # 조합 구하는 거 찾아보기(파이썬에 유용한 툴)
    # numbers = list(map(int, expression.split('+-*')))
    # print(numbers, tokens)
    priorities = [['+', '-', '*'], ['+', '*', '-'], ['*', '+', '-'], ['*', '-', '+'], ['-', '+', '*'], ['-', '*', '+']]
    ans_list = []
    for p in priorities:
        # print(p)
        nums = deque(numbers); toks = deque(tokens)
        p = deque(p)
        
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
                    rot_cnts = 0
                else:
                    nums.append(num1)
                    toks.append(cur_tok)
                    rot_cnts += 1
        ans_list.append(abs(nums[0]))

    print(max(ans_list))
    

    return max(ans_list)


solution("100-200*300-500+20")
solution("50*6-3*2")
solution("50")
solution("100-200-300-500-20")
solution("100-200*2*300*500-20")