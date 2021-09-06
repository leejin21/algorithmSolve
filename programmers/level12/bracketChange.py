# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
# 32분 53초컷
'''
균형잡힌: bal
올바른: right

u => 최소 bal
v => 그 나머지
'''
import sys; read = sys.stdin.readline
import collections

table = str.maketrans('()', ')(')

def checkRight(word):
    stack = collections.deque()
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if stack: return False
    return True


def solution(p):
    answer = ''
    if len(p) == 0:
        return ''
    bracket_cnts = collections.defaultdict(int)
    
    for i in range(len(p)):
        # print(bracket_cnts)
        bracket_cnts[p[i]] += 1
        if (bracket_cnts['('] == bracket_cnts[')']) and bracket_cnts['('] != 0:
            break
    
    u = p[:i+1]; v = p[i+1:]
    # print(u, v)
    if checkRight(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += u[1:-1].translate(table)
    
    return answer

print("sol", solution("(()())()"))
print("sol", solution(")("))
print("sol", solution("()))((()"))
# print(checkRight("((("))
# print(checkRight(")))"))
# print(checkRight(")("))
# print(checkRight("()()"))