'''

'''
import sys; read = sys.stdin.readline
import collections
import datetime

def solution(a, b):
    
    form = '2016-%s-%s'%(str(a), str(b))
    d = datetime.datetime.strptime(form, '%Y-%m-%d')
    answer = d.strftime('%a').upper()
    return answer
print(solution(5, 23))
print(solution(5, 24))
print(solution(5, 25))
print(solution(5, 26))
print(solution(5, 27))
print(solution(5, 28))
print(solution(5, 29))