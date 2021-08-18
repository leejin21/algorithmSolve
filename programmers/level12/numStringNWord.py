# 숫자 문자열과 영단어
# 30분 걸림.....


def solution(s):
    ans_list = []
    # 첫글자: [(마지막 글자, 마지막 알파벳이 나온 순번, 해당하는 숫자)]
    table = {'z': [('o',0, 0)], 'o': [('e', 0, 1)], 't': [('o', 0, 2), ('e', 1, 3)], 'f': [('r', 0, 4), ('e', 0, 5)], 's': [('x', 0, 6), ('n', 0, 7)], 'e': [('t', 0, 8)], 'n': [('e', 0, 9)]}

    def findWord(alp):
        for c in cands:
            if c[0] == alp:
                return c
        return None

    i = 0; mid = False; last_cnt = 0
    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord("9"):
            ans_list.append(int(s[i]))
            mid = False
            continue
        elif not mid:
            # 단어 첫 시작
            cands = table[s[i]]
            mid = True
        else:
            # 단어 중간
            word_info = findWord(s[i])
            if not word_info: continue
            if word_info[1] == last_cnt:
                ans_list.append(word_info[2])
                mid = False
                last_cnt = 0
            else:
                last_cnt += 1
            
    answer = 0
    for i in range(len(ans_list)):
        answer += ans_list[i]*pow(10, len(ans_list)-i-1)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))