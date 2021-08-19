# 신규 아이디 추천

'''
[카카오 아이디 규칙]
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.


.hellop
hello.p
hello..p..a
he
heeeeeeeeeeeeeeeeeeeeee
HELLO
hello33
hello_33


'''

def isIdAvailable(new_id):
    if len(new_id) > 15 or len(new_id) <3:
        return False
    if new_id[0] == '.' or new_id[len(new_id)-1] == '.':
        # .은 처음과 끝에 사용할 수 없음.
        return False
    dotcont = False
    for s in new_id:
        if s == '.':
            # 연속인 지
            if dotcont:
                return False
            dotcont = True
            continue
        else:
            dotcont = False
            if ord('a')<=ord(s)<=ord('z'):
                continue
            if ord('0')<=ord(s)<=ord('9'):
                continue
            if s == '-' or s == '_':
                continue
            return False

    return True
            
# print(isIdAvailable('.hellop'))
# print(isIdAvailable('hello.p'))
# print(isIdAvailable('hello..p..a')) 
# print(isIdAvailable('heeeeeeeeeeeeeeeeeeeeee'))
# print(isIdAvailable('he'))


def solution(new_id):
    answer = ''
    # if isIdAvailable(new_id):
    #     return new_id
    # 1단계
    new_id = new_id.lower()
    # print(1, new_id)

    # 2단계, 3단계
    new_id_lst = []
    dotcont = False
    for s in new_id:
        if s == '.':
            # 연속인 지
            if dotcont:
                continue
            dotcont = True
            new_id_lst.append(s)
        else:
            dotcont = False
            if ord('a')<=ord(s)<=ord('z'):
                new_id_lst.append(s)
            if ord('0')<=ord(s)<=ord('9'):
                new_id_lst.append(s)
            if s == '-' or s == '_':
                new_id_lst.append(s)
    # print(23, "".join(new_id_lst))
    
    # 4단계
    if len(new_id_lst) > 0 and new_id_lst[0] == '.':
        new_id_lst = new_id_lst[1:]
    if len(new_id_lst) > 0 and new_id_lst[-1] == '.':
        new_id_lst = new_id_lst[:-1]
    # print(4, "".join(new_id_lst))

    # 5단계
    if len(new_id_lst) == 0:
        new_id_lst.append('a')
    # print(5, "".join(new_id_lst))

    # 6단계
    if len(new_id_lst) >= 16:
        new_id_lst = new_id_lst[:15]
    if new_id_lst[-1] == '.':
        new_id_lst = new_id_lst[:-1]
    # print(6, "".join(new_id_lst))

    # 7단계
    end = new_id_lst[-1]
    while(len(new_id_lst)<=2):
        new_id_lst.append(end)
    # print(7, "".join(new_id_lst))

    return "".join(new_id_lst)

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("....24....."))
print(solution("b.....@"))
print(solution("b...cc..1"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
