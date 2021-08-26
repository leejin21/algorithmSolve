# 튜플

from collections import defaultdict

def solution(s):
    answer = []
    table = str.maketrans("{,}", "   ")
    s_list = list(map(int, s.translate(table).split()))
    s_dd = defaultdict(int)
    for i in s_list:
        s_dd[i] += 1

    answer = sorted(list(s_dd), key=lambda x: s_dd[x], reverse=True)
    # print(answer)
    return answer

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")