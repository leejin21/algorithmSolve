'''
문제가 잘못된 것 같음. 문제에서 말하는 건 완전 이진 트리가 아니라 포화 이진 트리인데..?
흠.. 그래도 맞음.


'''
import sys; read = sys.stdin.readline
from collections import deque
K = int(read())

inorder = [int(i) for i in read()[:-1].split(" ")]
front = 0; end = len(inorder)-1
stack = deque([(front, end)])

while(stack):
    tree_level = []
    next_stack = []
    while(stack):
        front, end = stack.popleft()
        mid = (end - front)//2 + front
        # print(front, end)
        tree_level.append(inorder[mid])
        # print(end, mid+1)
        if mid-1 >= front:
            # print((mid-1 - front)//2)
            next_stack.append((front, mid-1))
        if end >= mid+1:
            # print((end - mid+1)//2)
            next_stack.append((mid+1, end))

    for i in tree_level:
        print(i, end=" ")
    print("")
    stack += next_stack
    # print(stack)
    # i += 1
    # if i > 3:
    #     break