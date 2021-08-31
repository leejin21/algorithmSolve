# 상호 평가

'''
당신은 각 학생들이 받은 점수의 평균을 구하여, 기준에 따라 학점을 부여하려고 합니다.
만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.
'''



# sys.setrecursionlimit(10000)

def solution(scores):
    avg_lst = [0]*len(scores)
    grade_lst = ['Z']*len(scores)
    scores = list(map(list, zip(*scores)))
    
    # avg_lst = [0]*len(scores)
    # answer = 0
    for i, s in enumerate(scores):
        if (s[i] == max(s) and s.count(s[i]) == 1) or (s[i] == min(s) and s.count(s[i]) == 1):
            avg = (sum(s[0:i] + s[i+1:len(s)]))/(len(scores)-1)
        else:
            avg = sum(s)/len(scores)
        avg_lst[i] = avg
        if avg >= 90:
            grade_lst[i] = 'A'
        elif avg >= 80:
            grade_lst[i] = 'B'
        elif avg >= 70:
            grade_lst[i] = 'C'
        elif avg >= 50:
            grade_lst[i] = 'D'
        else:
            grade_lst[i] = 'F'
    # print(avg_lst)

    return ''.join(grade_lst)


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))