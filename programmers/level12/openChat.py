# 오픈채팅방
'''
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

이렇게 오래 걸릴 일이 아님........
결과를 상상하고 미리 쉬운 경로 찾기.
쓸데 없는 삽질 금지. 

'''
from collections import defaultdict
def solution(record):
    answer = []
    id_dict = defaultdict(dict)
    for i in range(len(record)):
        # print(record[i].split(" "))
        
        recs = record[i].split(" ")
        move = recs[0]; uid = recs[1]
        nickname = id_dict[uid]["nickname"] if recs[0] == 'Leave' else recs[2]
        
        id_dict[uid]["nickname"] = nickname
        try:
            # 저장할 때
            id_dict[uid]["move"][move].append(i)
        except:
            id_dict[uid]["move"] = defaultdict(list)
            id_dict[uid]["move"][move] = [i]
    
    answer_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for i in range(len(record)):
        recs = record[i].split(" ")
        move = recs[0]; uid = recs[1]
        if move == 'Change':
            continue
        else:
            answer.append(id_dict[uid]["nickname"] + answer_dict[move])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))