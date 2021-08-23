# 문자열 압축

'''
문자열 자르기.
2중 while문(기준1=단위, 기준2=iterate) 돌면서 문자열 단위로 잘랐을 때 가장 짧은 길이 찾아내기.
iterate하면서 연속하는 문자열 단위들 찾기

wswsaabbaabb
-> 2개로 자르면 2wsaabbaabb 로 나옴.

wsitititi

일단 원론적으로 풀자. 문제에서 제발 하라는 대로 풀자.. 꼼수 부리면 괜히 더 생각해야 됨.
X -> 12의 경우 어떡할 거임? 여기서 반례가 나온 거임.

'''

def solution(s):
    answer = len(s)
    unit_len = 1
    unit = ''
    while(unit_len <= len(s)//2):
        front = 0; end = unit_len
        unit = s[front:end]
        unit_lst = []
        it = 1
        # length = 0
        # print(unit)
        while(end < len(s)):
            front = end
            end = min(front + unit_len, len(s))
            # print(s[front:end])    
            if unit == s[front:end]:
                it += 1
            else:
                # length += 1 + unit_len if it else unit_len
                unit_lst.append(str(it)+unit if it>1 else unit)
                # print(length)
                unit = s[front:end]
                it = 1
            # print(unit_lst)
        # 마무리
        
        unit_lst.append(str(it)+unit if it>1 else unit)
        # print(''.join(unit_lst))
        # answer = min(answer, length)
        answer = min(answer, len(''.join(unit_lst)))
        # print(unit_len, answer)
        unit_len += 1
    return answer


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
print(solution("xabbaccabbaccabbacc"))
# -> ws3iti