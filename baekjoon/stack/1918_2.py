# 후위 표기식

'''
문제
수식은 일반적으로 3가지 표기법으로 표현할 수 있다. 연산자가 피연산자 가운데 위치하는 중위 표기법(일반적으로 우리가 쓰는 방법이다), 연산자가 피연산자 앞에 위치하는 전위 표기법(prefix notation), 연산자가 피연산자 뒤에 위치하는 후위 표기법(postfix notation)이 그것이다. 예를 들어 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

이 문제에서 우리가 다룰 표기법은 후위 표기법이다. 후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다. 이 방법의 장점은 다음과 같다. 우리가 흔히 쓰는 중위 표기식 같은 경우에는 덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만 후위 표기식을 사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다. 또한 같은 방법으로 괄호 등도 필요 없게 된다. 예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다. 우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다. 마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

다른 예를 들어 그림으로 표현하면 A+B*C-D/E를 완전하게 괄호로 묶고 연산자를 이동시킬 장소를 표시하면 다음과 같이 된다.

이러한 사실을 알고 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오

입력
첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 A~Z의 문자로 이루어지며 수식에서 한 번씩만 등장한다. 그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다. 


A + B*C - (D+E)*F + G/(H-I*J) - \
    (K*(L-M))/O
A + B*C - (D+E)*F + G/(H-I*J) - K*(L-M)/O

형식

(A) * (B) => (A)(B)*
(A) + (B) => (A)(B)+

A B +
A B *

[규칙]
A * B + C
 => (A * B) + C
A + B * C
 => A + (B * C)
A + B + C
 => (A + B) + C
(A + B) * C

<<하향식으로 처리>>

+ - 
-> root로 처리, 나머지는 left랑 right에 자식으로 처리.
* /
-> root로 처리, 나머지는 left랑 right에 자식으로.
( )
-> 이 안에서 똑같이 main 한번 더 돌리기: root 뽑아내기

출력
첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오

ABC+*


하 진짜 개 어렵네....
이틀째 못 푸는 중...

'''

from collections import deque
class Node:
    def __init__(self, tok):
        self.tok = tok
        self.lchild = None
        self.rchild = None
    

def printPostfix(root):
    if root:
        printPostfix(root.lchild)
        printPostfix(root.rchild)
        print(root.tok, end="")

def main(root):
    notation = root.tok
    if len(notation) > 1:
        end = notation.pop()
        if end == ')':
            right = makeBracket2Deq()
            tok = notation.pop()
            if tok in ['+', '-']:
                left = notation
            elif tok in ['*', '/']:
                left = makeBracket2Deq(right, notation) if notation[-1] == ')' else notation.pop()
                
                # 여기 오류: A + (B * C) * (D * E)
                # -> 덩어리로 취급해야 함.
            root.tok = tok
            root.rchild = right
            root.lchild = left
        elif ord('A')<=ord(end)<=ord('Z'):
            tok = notation.pop()
            
            left = make2List if notation[-1] == ')' else notation

        else:
            pass
    return root




def makeBracket2Deq(fromdeq, notation):
    q = deque() if not fromdeq else fromdeq
    while(True):
        temp = notation.pop()
        if temp == '(':
            return q
        q.appendleft(temp)



infix = input()
stack = deque([i for i in infix])
root = main(Node(stack))
# i = len(infix)-1
# print(stack)

while(stack):
    end = stack.pop()
    if end == ')':
        stack.append(make2List())
    elif type(end) == list:
        pass
    elif ord('A')<=ord(end)<=ord('Z'):
        tok = stack.pop()
        if tok == ')':
            stack.append(make2List())
        elif tok in ['*' or '/']:
            front = stack.pop()
            if front == ')':
                front = make2List()
            
        elif tok in ['+' or '-']:
            pass
