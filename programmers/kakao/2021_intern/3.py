'''
4:20에 진입.
다음으로 "D 4"를 수행한 다음 "C"를 수행한 후의 표 상태는 아래 그림과 같습니다. 5행이 표의 마지막 행 이므로, 이 경우 바로 윗 행을 선택하는 점에 주의합니다.

처음 표의 행 개수를 나타내는 정수 n, 처음에 선택된 행의 위치를 나타내는 정수 k, 수행한 명령어들이 담긴 문자열 배열 cmd가 매개변수로 주어질 때, 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

cmd
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.


8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

-> "OOOOXOOO"

8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

-> "OOXOXOOO"

deleted = [5]

2 3 4 0 1

'z'

[일단 왼쪽 방향으로만 rotate 시키기]
5보다 작은 최대 수보다 한번 더 rotate. = rotate 수: 3

3 4 0 1 | 2
4 0 1 | 2 3

0 1 | 2 3 4

5 appendleft

5 0 1 | 2 3 4

다시 원래 자리로 돌아가기 = rotate 수: (len(q)+1 - 방금 rotate수):정방향 또는 방금 rotate수:역방향 만큼 rotate

2 3 4 5 0 1


5 7 8 /
restore = 3, 6, 10
1.  5 7 8 / 3: 모두 작은 경우
[] [3] [5 7 8 3]
2. 6 : 중간인 경우
[7 8] [6 7 8] [5 6 7 8]
3. 10: 모두 큰 경우
[] [10] [5 7 8]


3 4 1 /
restore = 2, 0, 5
1. 3 4 1 / 2: 중간인 경우
[] [2] [3 4 1 2]
2. 3 4 1 / 0: 모두 작은 경우
[1] [0 1] [3 4 0 1]
3. 3 4 1 /5: 모두 큰 경우
[1] [5 1] [3 4 5 1]

3 4/ 5:
[] [5] [3 4 5]



'''
from collections import deque

def solution(n, k, cmd):
    q = deque(range(n)); deleted = []
    q.rotate(-1*k)
    # print(q)
    for c in cmd:
        # print(c)
        if c[0] == 'D':
            q.rotate(-1*int(c[2]))
        elif c[0] == 'C':
            deleted.append(q.popleft())
            if len(q)>0 and deleted[-1] > q[0]:
                q.rotate(1)
        elif c[0] == 'U':
            q.rotate(int(c[2]))
        elif c[0] == 'Z':
            temp_list = []; restore = deleted.pop()
            if len(q) > 0 and q[0] < q[-1]:
                if restore < q[0] or restore > q[-1]:
                    while(q): temp_list.append(q.popleft())
                elif q[0]<restore<q[1]:
                    while(q[0]<restore): 
                        temp_list.append(q.popleft())
            elif len(q) > 0 and q[0] > q[-1]:
                if restore < q[-1] or restore > q[0]:
                    while(q): 
                        if temp_list and temp_list[-1] > q[0]:
                            # 작아지는 지점에서 break
                            break
                        temp_list.append(q.popleft())
                elif q[-1]<restore<q[0]:
                    while(q): temp_list.append(q.popleft())
            else:
                temp_list.append(q.popleft())
            # print('아', q, temp_list)
            q.appendleft(restore)
            # print('아하', q)
            while(temp_list):
                q.appendleft(temp_list.pop())
            

        # print(q, deleted)

    answer = ['O' for _ in range(n)]
    for i in deleted:
        answer[i] = 'X'

    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
print(solution(5, 0, ["C", "C", "C", "Z", "Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))