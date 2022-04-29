# 감시

'''
[브루트 포스]
1. cctv에서 방향 결정을 dfs로 진행
    1.1 dfs가 되는 방식은 다음 예시와 같다.
        0_0_0 ~ 0_1_0 ~ 1_0_0 ~ ...
        0_0_1 ~ 0_1_0 ~ 1_0_0 ~ ...
        
        이때, k_m_l이면 k번 cctv 종류인 m번쨰 cctv가 l 쪽 방향으로 진행되는 경우를 말하며,
        해당하는 경우들을 모든 cctv에 대해 조합(모든 경우의 수)을 구한다.

        1.1.1 l쪽 방향에서 l은 2번 종류의 cctv의 경우 [(왼-오), (위-아래)] 이 2개 종류 중 하나로 될 수 있다.
    
    1.2 5번 cctv에 대해 방향 결정을 끝내면 -> 사각지대를 계산해서: 사각지대에 해당하는 0을 카운트한다.
    1.3 1.1 ~ 1.2에서 진행한 모든 경우의 수에 대해 사각지대 개수가 최소가 되는 값을 찾아서 리턴해 준다.
'''
import sys

def goStraight(c_i: int, c_j: int, office: list, d: int):
    # 벽 고려 시: cctv_k에서 뻗어나가는 방향으로 가다가 멈춤
    # 한쪽 방향만 우선 고려

    d_range = {
        # d = 위0, 오른1, 아래2, 왼3
        0: range(c_i-1, -1, -1),
        1: range(c_j+1, len(office[0])),
        2: range(c_i+1, len(office)),
        3: range(c_j-1, -1, -1)
    }

    for k in d_range[d]:
        if d == 0 or d == 2:
            if office[k][c_j] == '6':
                break
            office[k][c_j] = '#'
        elif d == 1 or d == 3:
            if office[c_i][k] == '6':
                break
            office[c_i][k] = '#'
    

def main(M: int, N: int, office: list):
    cctvs = {'1': [], '2': [], '3': [], '4':[], '5':[]} # 'cctv 종류': 'cctv idx (i, j)'
    cctv_dir_combs = {'1': [[0], [1], [2], [3]], '2':[[0,2], [1,3]], '3':[[0, 1], [1, 2], [2, 3], [3, 0]], '4':[[0,1,2], [0,1,3], [0,2,3], [1,2,3]], '5':[[0,1,2,3]]} #  
    
    # cctvs 생성
    for i in range(M):
        for j in range(N):
            if 1 <= int(office[i][j]) <= 5:
                cctvs[office[i][j]].append((i, j))

    min_blind_spot_cnt = sys.maxsize

    def dfs(cctv_num: int, cctv_i: int, office_board: list):
        # dfs가 돌아가는 단위: cctv 1개(cctv 종류 중 1개에 해당)
        nonlocal cctvs, cctv_dir_combs, min_blind_spot_cnt

        if cctv_num > 5:
            # cctv_num이 5번을 넘어가면 사각지대 카운트하고 dfs stop
            cnt = 0
            for o in range(len(office_board)):
                for y in range(len(office_board[0])):
                    if office_board[o][y] == '0':
                        cnt += 1
            min_blind_spot_cnt = min(cnt, min_blind_spot_cnt)
            return
        
        if len(cctvs[str(cctv_num)]) == 0:
            # cctv_num번 cctv가 이번에 존재하지 않을 경우 다음 cctv_num번으로 넘어가도록 함
            next_cctv_num = cctv_num + 1
            dfs(next_cctv_num, 0, office_board)
            return

        for d_num in range(len(cctv_dir_combs[str(cctv_num)])):
            temp_office = [row[:] for row in office_board]
                # 매번 temp_office를 deep copy해서 이번 방향에 대해 dfs 보내기

            c_i, c_j = cctvs[str(cctv_num)][cctv_i]
            for d in cctv_dir_combs[str(cctv_num)][d_num]:
                # 이번 방향에 대해 temp_office에 표시하기(감시할 수 있는 부분들 표기)
                goStraight(c_i, c_j, temp_office, d)

            if cctv_i >= len(cctvs[str(cctv_num)])-1:
                next_cctv_num = cctv_num + 1
                next_cctv_i = 0
            else:
                next_cctv_num = cctv_num
                next_cctv_i = cctv_i + 1

            # 다음 dfs 턴으로 넘어가기
            dfs(next_cctv_num, next_cctv_i, temp_office)
                
    dfs(1, 0, office)
    return min_blind_spot_cnt
        


N, M = [int(i) for i in input().split(" ")]
office = [[i for i in input().split(" ")] for _ in range(N)] # office 는 2차원 문자열 배열

print(main(N, M, office))
