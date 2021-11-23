# 조이스틱
# 미완
'''
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
'''
def solution(name):
    answer = 0
    bef = 0; aft = 0
    for i, alp in enumerate(name):
        if alp == 'A' and (i == 0 or name[i-1] != 'A'):
            # 처음 A 시작
            bef = i-1 if i!= 0 else 0
        elif i!= 0 and alp != 'A' and name[i-1] == 'A':
            aft = i

        # print(ord(alp)-ord('A'))
        # print(ord('Z')-ord(alp)+1)
        # 커서 수직적으로 움직이는 횟수
        answer += min(ord(alp)-ord('A'), ord('Z')-ord(alp)+1)
    # 커서 수평적으로 움직이는 횟수
    return answer

print(solution('JAN'))