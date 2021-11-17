# 압축
'''
무손실 압축 알고리즘 구현하기

    길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
    w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
    입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
    단계 2로 돌아간다.
'''
import sys; read = sys.stdin.readline
import collections
import string


def solution(msg):
    answer = []
    #* 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    d = collections.defaultdict(int)
    for i,j in enumerate(string.ascii_uppercase):
        d[j] = i+1
    cur_idx = 0
    while(cur_idx<len(msg)):
        #* 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        MAX_STRING = ''
        MAX_STRING_Y = cur_idx
            # MAX_STRING의 마지막 char의 인덱스
        # print(cur_idx)
        for i in range(cur_idx+1, len(msg)+1):
            if d[msg[cur_idx:i]] != 0:
                MAX_STRING = msg[cur_idx:i]
                MAX_STRING_Y = i-1
            else:
                # 가장 긴 문자열 w는 현재 MAX_STRING으로 확정
                break
        # print(MAX_STRING)
        #* 3. w에 해당하는 사전의 색인 번호를 출력
        answer.append(d[MAX_STRING])
        #* 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if MAX_STRING_Y+1<len(msg):
            d[MAX_STRING+msg[MAX_STRING_Y+1]]=len(d.keys())
        #* 5. 입력에서 w를 제거한다.
        cur_idx = MAX_STRING_Y + 1
    # print(d)
    return answer

print(solution('KAKAO'))