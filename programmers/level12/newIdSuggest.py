# 신규 아이디 추천

'''
[카카오 아이디 규칙]
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

[반례]
.$$$.%%%.. 이경우가 반례였던 듯.
-> 2,3 단계 같이 처리해서 문제가 됨.

'''


def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    table = str.maketrans("~!@#$%^&*()=+[{]}:?,<>/","                       ")
    new_id = new_id.translate(table)
    new_id = "".join(new_id.split())

    # 3단계
    while True:
        if new_id.find("..") != -1:
            new_id = new_id.replace("..", ".")
        else:
            break
    
    # 4단계
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계
    end = new_id[-1]
    while(len(new_id)<=2):
        new_id += end

    return new_id

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("....24....."))
print(solution(''))
print(solution("b.....@"))
print(solution("b...cc..1"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
