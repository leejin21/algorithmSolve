'''
종이의 개수
문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

(1) 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(2) (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

3
0 0 0
0 0 0
0 0 0

9
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 1 1 1 0 0 0

3
-1 0 1
0 -1 1
1 1 0


3
0 0 1
0 0 0
0 0 0
'''
import sys; read = sys.stdin.readline
sys.setrecursionlimit(3000)
CNT = {-1: 0, 0: 0, 1:0}

def cutPaper(paper):
    global CNT
    n = len(paper)
    # 9개의 동일한 크기로 잘라주기
    # 자르고 거기서 또 cutPaper 해주기
    # 종결: 현 paper 크기 == 1이거나 모두 같은 수로 되어있으면 멈춰!
    # print(paper)
    if len(paper) == 1:
        CNT[paper[0][0]] += 1
    elif isAllSame(paper):
        CNT[paper[0][0]] += 1
    else:
        i_paper = []
        for i in range(3):
            i_paper = paper[i*n//3:(i+1)*n//3]
            # print("ipaper", i_paper)
            for j in range(3):
                # print("i, j:", i, j)
                next_paper = []
                for k in range(n//3):
                    front = j*n//3
                    end = (j+1)*n//3
                    # print("k, front, end", k, front, end)
                    next_paper.append(i_paper[k][front:end])
                # print("next_paper", next_paper)
                cutPaper(next_paper)
                
                

def isAllSame(paper):
    d = {-1: (0,1), 0: (-1, 1), 1: (-1, 0)}
    std = paper[0][0]; c1, c2 = d[std]
    for row in paper:
        if c1 in row or c2 in row:
            return False
    return True


N = int(read())
paper = list(map(lambda _: list(map(int, read().split(" "))), range(N)))
# print(paper)
cutPaper(paper)

print(CNT[-1])
print(CNT[0])
print(CNT[1])