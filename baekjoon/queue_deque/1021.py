# 회전하는 큐
'''
문제
지민이는 N개의 원소를 포함하고 있는 "양방향 순환 큐"를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 "주어진 순서대로" 뽑아내는데 드는 2번, 3번 "연산의 최솟값"을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

SOLUTION
deque도 list처럼 인덱싱 가능.
문제 잘 읽자. 중요한 부분 확인해보기: 주어진 순서대로를 못 봤음.

rotate(양수): 오른쪽으로 감.
rotate(음수): 왼쪽으로 감.

* 

'''
# 양방향 순환 큐
from collections import deque

def main():
    N, _ = (int(i) for i in input().split())
    deq = deque(range(1, N+1))
        # 큐
    ob_list = deque([[int(o), int(o)-1] for o in input().split()])
        # 뽑아내야 하는 수들: (수, que에서 수의 위치)
    print(deq, ob_list)
    tot_move = 0; cnt = 0

    for o, i in ob_list:
        if i != 0:
            l_move = i; r_move = N-i
            if l_move < r_move:
                # 왼쪽으로 움직이기
                deq.rotate(-l_move)
                isLeftMove = True; move = l_move

            else:
                # 오른으로 움직이기
                deq.rotate(r_move)
                isLeftMove = False; move = r_move

            for x in range(cnt, len(ob_list)):
                # 움직인 결과 반영
                change = calcIdxChng(ob_list[x][1], i, len(deq), isLeftMove, move)
                ob_list[x][1] -= change - 1 if isLeftMove else -change + 1
                print(ob_list, change-1)

        else: 
            move = 0; isLeftMove="Zero"
            for x in range(cnt, len(ob_list)):
                # 움직인 결과 반영
                ob_list[x][1] -= 1
            
        deq.popleft()
        tot_move += move
        cnt += 1

        print(isLeftMove, move, tot_move)
        print(cnt, deq)
        print(ob_list)
        
    print(tot_move)
        
    
def calcIdxChng(ob_i, cur_i, len_deq, isLeftMove, move):
    if (ob_i > cur_i and isLeftMove) or (ob_i < cur_i and not isLeftMove):
        # 왼쪽으로 움직였을 때 뽑는 원소의 오른쪽에 위치한 원소들의 인덱스 변화
        # 또는 오른쪽으로 움직였을 때 뽑는 원소의 왼쪽에 위치한 원소들의 인덱스 변화
        return move
    else:
        # 오른으로 움직였을 때 뽑는 원소의 오른쪽에 위치한 원소들의 인덱스 변화
        # 또는 왼쪽으로 움직였을 때 뽑는 원소의 왼쪽에 위치한 원소들의 인덱스 변화
        return - len_deq + move

main()
