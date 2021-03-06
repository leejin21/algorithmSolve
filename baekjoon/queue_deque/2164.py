# 카드 2
'''
문제
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

출력
첫째 줄에 남게 되는 카드의 번호를 출력한다


[SOLUTION]
* list는 pop(0)의 연산이 O(n)이라고 함.
* 그래서 python 공식 docs에서도 리스트는 큐로 쓰는 걸 권장하지 않는다고 함.
차라리 collections의 deque을 쓰라고 함.
* deque
    - popleft
    - pop
    - append
    - appendleft

    나머지 extend, extendleft, rotate은 O(k)의 시간 복잡도를 가짐
    remove는 O(n)의 시간 복잡도를 가짐

* 1번 시도: 
마지막 한 장 남았으면 어차피 맨 뒤로 보내므로 그냥 return해 버리기의 의도로
cards.popleft() 다음으로 len(cards)==1을 검사해서 return해 주었으나,
N = 1의 경우 그렇게 되면 while문에서 영원히 못 빠져나와서 런타임에러 생김.

* 2번 시도:
N = 1의 경우를 따로 빼 줌.
'''
from collections import deque

def main():
    N = int(input())
    cards = deque(range(1, N+1))
    if N == 1:
        return 1
    while(True):
        
        # 맨 앞 장 바닥에 버리기
        cards.popleft()
        
        if len(cards) == 1:
            return cards.pop()
            
        # 다음 앞 장 맨 뒤로 보내버리기
        top = cards.popleft()
        cards.append(top)       
    

print(main())