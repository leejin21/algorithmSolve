# 균형잡힌 세상
'''
문제
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

+ 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
+ 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
+ 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
+ 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
+ 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

입력
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.


SOLUTION
[1번 시도]
* T의 마지막 문자열=. 이 유일무이할 거라고 생각해서 for문의 break조건으로 "."을 걸어뒀다.

[2번 시도]
* for문의 형태를 바꿔서 T의 길이와 현재 인덱스 위치를 비교하는 방식으로 for문의 break조건을 걸어둠
* 이렇게 해야 문장 끝까지 다 검사한 후 이상이 다 없으면 yes를 answers 리스트에 추가해 줌.


'''

stack = []

def main():
    global stack
    answers = []
    while(True):
        T = input()
        if T == ".": break  # 종료 조건
        for i in range(len(T)):
            if T[i] in ['(', '[']:
                # T의 i번째 문자가 여는 괄호일 경우, 스택에 추가만 하기
                stack.append(T[i])
            elif T[i] in [')', ']']:
                # T의 i번째 문자가 닫는 괄호일 경우, 스택의 top과 비교해서 맞물리지 않으면 NO
                ans = close(T[i])
                if not ans:
                    answers.append('no')
                    break
            if i == len(T)-1 and len(stack)==0:
                # T를 끝까지 하고 스택이 깨끗하면 YES
                answers.append('yes')
            elif i == len(T)-1 and len(stack)!=0:
                # T가 끝까지 되었는데 스택에 뭐가 잔여해 있으면 NO
                answers.append('no')
            
        stack = []
    
    for ans in answers:
        print(ans)
        

def close(c):
    global stack
    matches = {')':'(', ']':'['}
    if len(stack) != 0:
        top = stack.pop()
        if top == matches[c]:
            return True
        else:
            return False
    else:
        return False


main()