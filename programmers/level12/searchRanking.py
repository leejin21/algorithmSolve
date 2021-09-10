# 효율성 테스트에서 틀림 판정, 정확성 테스트는 맞음.
'''
16개의 케이스로 딕셔너리에 키로 저장, 밸류 = [점수]

cpp, java, python, -
backend, frontend, -
junior, senior, -
chicken, pizza, -

'''
import sys; read = sys.stdin.readline
import collections


def solution(info, query):
    answer2 = []
    lang_info = collections.defaultdict(list)
    end_info = collections.defaultdict(list)
    year_info = collections.defaultdict(list)
    food_info = collections.defaultdict(list)
    point_info = []

    tot = len(info)
    for i, v in enumerate(info):
        lang, end, year, food, point = v.split()
        lang_info[lang].append(i)
        end_info[end].append(i)
        year_info[year].append(i)
        food_info[food].append(i)
        point_info.append(int(point))
    
    lang_info['-']+=list(range(len(info)))
    end_info['-']+=list(range(len(info)))
    year_info['-']+=list(range(len(info)))
    food_info['-']+=list(range(len(info)))

    for q in query:
        q_list = q.split()
        
        cnt = 0
        lang = q_list[0]
        end = q_list[2]
        year = q_list[4]
        food = q_list[6]
        minpoint = int(q_list[7])
        # 여기에서 효율성에 너무 오래 걸리는 것 같음.
        # 각 set을 만들어서...
        
        answer = set(lang_info[lang])&set(end_info[end])&set(year_info[year])&set(food_info[food])
        # print(answer)
        # print(point_info)
        for a in answer:
            # print(a, point_info[a], minpoint)
            if point_info[a] >= minpoint:
                cnt += 1
        answer2.append(cnt)
    
    return answer2

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))