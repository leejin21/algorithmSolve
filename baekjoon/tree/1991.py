# 트리 순회
'''
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.


'''
import sys; read = sys.stdin.readline
import collections

class Node:
    def __init__(self, alp, left, right):
        self.alp = alp
        self.left = left
        self.right = right

def saveNode(alp):
    if not nodes[alp] and alp != '.':
        nodes[alp] = Node(alp, None, None)

def order(root, what):
    if root:
        if what == 'pre': print(root.alp, end='')
        order(root.left, what)
        if what == 'in': print(root.alp, end='')
        order(root.right, what)
        if what == 'post': print(root.alp, end='')

N = int(read())
nodes = collections.defaultdict(int)
for _ in range(N):
    parent, left, right = read().split()
    saveNode(parent); saveNode(left); saveNode(right)

    # left 추가
    if left != '.': nodes[parent].left = nodes[left]
    if right != '.': nodes[parent].right = nodes[right]

# print_tree()
for what in ['pre', 'in', 'post']:
    order(nodes['A'], what); print()

######################################################################
def print_tree():
    # 문제에 쓸모 X
    for key, value in nodes.items():
        print(key, end=' ')
        if key != '.' and value.left: print(value.left.alp, end=' ')
        else: print(end=' ')
        if key != '.' and value.right: print(value.right.alp, end=' ')
        else: print(end=' ')
        print(' ')
