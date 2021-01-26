# 2263.py
# 트리의 순회
'''
PROBLEM

n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1≤n≤100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.
3
1 2 3
1 3 2

출력
첫째 줄에 프리오더를 출력한다.
2 1 3
'''

'''
SOLUTION

try 1: 메모리 초과
배열에서 슬라이스로 넘길 때 매번 새로운 배열을 만들기 때문에 슬라이스로 넘기면 안됨

try 2: 틀림
인덱스를 함수 인자로 넘겨서 재귀를 구성했는데 p_right_stt나 p_left_end는 in_left의 길이 + 현재 p_stt를 해 줘야 재귀로 right 부분 처리할 때 인덱스가 0으로 갑자기 내려가지 않는다.

try 3: 런타임 에러 (RecursionError)
for문으로 재귀 넘겨주기

try 4: 시간 초과
in_location[inorder_value] = inorder_index
로 rid = inorder.index(root)를 줄임.
'''
preorder = []
porder = []; inorder= []; in_location = []

def main():
    global preorder, porder, inorder, in_location
    # * INITIALIZATION
    N = int(input())
    porder, inorder = saveInput(N)
    in_location = [0]*(N+1)
    for i, v in enumerate(inorder):
        in_location[v] = i
    # print(in_location)
    # * MAIN CODE
    # getPreOrder(0, len(porder)-1, 0, len(inorder)-1)
    whileGetPreOrder()
    
    # showOutput()

def whileGetPreOrder():
    global in_location
    stack = []
    stack.append([0, len(porder)-1, 0, len(inorder)-1])
    while(len(stack) != 0):
        in_stt, in_end, p_stt, p_end = stack.pop()
        if (p_end-p_stt > -1 and p_stt > -1 and p_end < len(porder) and in_end - in_stt > -1):
            root = porder[p_end]
            # rid = inorder.index(root)
            rid = in_location[root]
            # preorder.append(root)
            print(root, end=" ")
            
            if (p_end-p_stt != 0 and in_end-in_stt != 0):
                in_left_stt = in_stt; in_left_end = rid-1
                in_right_stt = rid+1; in_right_end = in_end
                
                p_left_stt = p_stt; p_left_end = in_left_end - in_left_stt + p_stt
                p_right_stt = in_left_end - in_left_stt + p_stt+ 1; p_right_end = p_end - 1
                
                # stack에서는 선입후출로 진행되기 때문에 r => l을 방지하기 위해 재귀와는 반대로 해 줌.
                stack.append([in_right_stt, in_right_end, p_right_stt, p_right_end])
                stack.append([in_left_stt, in_left_end, p_left_stt, p_left_end])


def saveInput(N):
    # 인풋 관리 및 저장
    
    inorder = [int(i) for i in input().split()]
    porder = [int(i) for i in input().split()]
    return porder, inorder
    # print(postorder, inorder)

# print(main())
main()


def getPreOrder(in_stt, in_end, p_stt, p_end):
    # index만 넘기기
    global porder, inorder, preorder
    if (p_end-p_stt > -1 and p_stt > -1 and p_end < len(porder) and in_end - in_stt > -1):
        root = porder[p_end]
        rid = inorder.index(root)
        preorder.append(root)
        
        if (p_end-p_stt != 0 and in_end-in_stt != 0):
            in_left_stt = in_stt; in_left_end = rid-1
            in_right_stt = rid+1; in_right_end = in_end
            
            p_left_stt = p_stt; p_left_end = in_left_end - in_left_stt + p_stt
            p_right_stt = in_left_end - in_left_stt + p_stt+ 1; p_right_end = p_end - 1

            # print("LEFT")
            # print("in_stt", in_left_stt, "in_end", in_left_end, "p_stt", p_left_stt, "p_end", p_left_end)

            # print("RIGHT")
            # print("in_stt", in_right_stt, "in_end", in_right_end, "p_stt", p_right_stt, "p_end", p_right_end)
            getPreOrder(in_left_stt, in_left_end, p_left_stt, p_left_end)
            getPreOrder(in_right_stt, in_right_end, p_right_stt, p_right_end)

def showOutput():
    for i, v in enumerate(preorder):
        if i != len(preorder) -1:
            print(v, end=" ")
        else:
            print(v)
