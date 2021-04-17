# 체스판 다시 칠하기
'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

1


SOLUTION
체스판의 왼쪽 위가 j, i 일때 
i 후보: 0 ~ N-8
j 후보: 0 ~ M-8

시간 복잡도는 따라서 O(NM)

try1: O(MN*8*8)
매 i, j 후보마다 해당 범위 내의 칠하는 부분을 체크해서(8*8) 더하기

-> 오류: cntB와 cntW 두개로 나뉘어야 한다고 함.
이유 = 왼쪽 위가 블랙이고, 나머지는 왼쪽 위만 바꾸면 되는.. 그런 구성일 수 있기 떄문
****왼쪽위는 고정값이 아니기 떄문!!!*****

try2:
따라서 왼쪽 위에서부터 어느 j,i번쨰 인덱스가 짝수만큼 먼 경우
짝수만큼 먼 인덱스에 b로 규칙을 맞춰 색칠하게 되는 경우 = b_cnt
                w로 규칙을 맞춰 색칠하게 되는 경우 = w_cnt

그래서 b_cnt, w_cnt 중 나중에 덜 추가되는 걸로.


*******무턱대로 하지말고 예시 딱 하나라도 들어서 한번 해 보기...*********
'''


def main():
    M,N = map(lambda i: int(i), input().split())
    board = list(map(lambda i: input(), range(M)))
    BMIN = 100; WMIN = 100

    for i in range(N-8+1):
        for j in range(M-8+1):
            bcnt = 0; wcnt = 0; f_val = board[j][i]
            for x in range(i, i+8):
                for y in range(j, j+8):
                    if ((x+y-(i+j)) % 2) == 0:
                        # i,j 로부터 짝수만큼 떨어져 있음
                        if board[y][x] == 'B':
                            wcnt += 1
                        else:
                            bcnt += 1
                    else:
                        if board[y][x] == 'B':
                            bcnt += 1
                        else:
                            wcnt += 1
                    
            BMIN = min(bcnt, BMIN)
            WMIN = min(wcnt, WMIN)

    return min(BMIN, WMIN)

print(main())