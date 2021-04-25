'''
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]

1: 4 [4]
5: 3 [4 3]
3: 1 [4 3 1]
5: 1 [4 3]
펑
1: 3 [4]
펑
2: 2 [4 2]
1: 아무것도 없음 [4 2]
4: [4 2 4]

스택 큐 이용하는 문제. 특징 파악 후 풀기 시작했어야 함.
'''

def solution(board, moves):
    stack = []; answer = 0
    board_stacks = [None]*len(board[0])

    for j in range(len(board[0])):
        board_stacks[j] = []
        for i in range(len(board)-1, -1, -1):
            # 거꾸로 들어가야 함
            if board[i][j]: board_stacks[j].append(board[i][j])
    
    for move in moves:
        if board_stacks[move-1]:
            doll = board_stacks[move-1].pop()
            if stack and stack[len(stack)-1] == doll:
                stack.pop(); answer += 2
            else:
                stack.append(doll)
    return answer



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))