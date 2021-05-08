'''
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

케이스
1. one4
 즉 one, 4
2. 4one

3. onetwo

1. 숫자 기준으로 분리해주기.
one 4 seveneight
23 four 5 six 7
1 zerotwozero 3

2. 알파벳으로 구분해서 words 처리해주기
1 4 seven/eight
-> 1 4 7 8

3. 리스트 => join해서 int형으로 바꿔주기.

'''

def solution(s):
    words = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    word_ends = {"z": ["o"], "o":["e"], 't':['o','e'], 'f':['r','e'], 's':['x', 'n'], 'e':['t'], 'n':['e']}

    # z:o o:e t:o t:e2 f:r f:e s:x s:n e:t n:e
    answer = []; end = True; w = []; t_first = True
    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'): 
            # 숫자인 경우
            answer.append(s[i])
        else:
            # 알파벳인 경우
            if end:
                # 단어의 새 시작
                w.append(s[i])
                end = False
            else:
                # 이미 단어 시작한 경우
                if s[i] in word_ends[w[0]]:
                    # end에 해당
                    w.append(s[i])
                    if w[0]=='t' and s[i]=='e' and t_first:
                        # three의 경우
                        t_first = False
                        continue
                    end = True
                    answer.append(words[''.join(w)])
                    w = []; t_first = True
                else:
                    w.append(s[i])

    return int(''.join(answer))

print(solution('123'))