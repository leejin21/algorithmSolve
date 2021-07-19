# 이진 검색 트리

'''
이진 검색 트리 전위순회 => 후위 순회한 결과 가져 오기



'''
import sys; read = sys.stdin.readline
from collections import deque

preOrder = deque()

class Node:
    def __init__(self, num):
        self.num = num
        self.left =None
        self.right = None

def main():
    # preorder append
    while(True):
        try:
            preOrder.append(int(read()))
        except:
            break
    # print(preOrder)
    head = makeTree(preOrder)
    
    print("post order")
    postOrder(head)

def makeTree(preOrder):
    # make tree
    # print("make tree")
    temp = Node(preOrder.popleft())
    stack = deque([temp])
    head = temp
    while(preOrder):
        new_node = Node(preOrder.popleft())
        print("새로운 new_node", new_node.num)
        if temp.num > new_node.num:
            print(temp.num, ">", new_node.num)
            temp = stack.pop()
            temp.left = new_node
            stack.append(temp)
            temp = new_node
            stack.append(new_node)
        else:
            while(stack):
                printStack(stack)
                temp = stack.pop()
                print(temp.num)
                if temp.num > new_node.num:
                    temp.left.right = new_node
                    break
                    
            if not stack:
                temp.right = new_node
            else:
                stack.append(temp)
            temp = new_node
        
    return head

# post order
def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.num)

def printStack(stack):
    print("print stack")
    for s in stack:
        print(s.num, end=" ")
    print("====")

main()