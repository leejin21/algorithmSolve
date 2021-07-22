# 거짓말

'''
진실된 이야기 듣고 => 과장된 이야기 들으면 탄로남.
과장된 이야기 듣고 => 진실된 이야기 들으면 탄로남.

for문으로 하면 안됨.

--반례--
앎: 2
모름: 9 10
파티는
9 10
2 9 10


--반례--
앎: 2
ppl수: 10

1 2 -
1 3 -
3 4 -
4 5 -
5 6 -

=> 이런 경우 모두 다 진실을 말해야 함.

[while 패턴]
진실을 이미 아는 애들과 속한 파티의 사람들을 먼저 진실을 안다고 필터링을 해 줌(큐에서 제거하는 방식)
그래서 진실을 (미래, 과거, 현재에) 아는 사람들을 더 찾으면 => 또 while문
못 찾으면 => 멈춤.

결과인 pplWhoKnowTruth를 가지고 진실을 말할 수 있는 파티를 찾음.

'''
import sys; read = sys.stdin.readline
from collections import deque

N, M = list(map(int, read()[:-1].split(" ")))
knowtruth = list(map(int, read()[:-1].split(" ")))[1:]
# print(N, M, knowtruth)
pplWhoKnowTruth = [False]*(N+1)
#0: 무지성, 1: 진실을 앎 

msg_party = 0
# party_q = deque()
party_list = []

for p in knowtruth:
    pplWhoKnowTruth[p] = True

for m in range(M):
    party_list.append(list(map(int, read()[:-1].split(" ")))[1:])
party_q = deque(party_list)

q_len = len(party_q); len_same = 0
    # q_len이랑 len_same으로 q에 남은 게 무지성 참가자들만의 파티일 때까지 while문 지속
while(party_q and q_len > len_same):
    party_data = party_q.popleft()
    q_len -= 1
    thisPartyTruth = False
    for pnum in range(len(party_data)):
        # pnum = participant num(참여자 번호)
        if pplWhoKnowTruth[party_data[pnum]]:
            thisPartyTruth = True
            break
    if thisPartyTruth:
        len_same = 0
        for pnum in range(len(party_data)):
            pplWhoKnowTruth[party_data[pnum]] = True
    else:
        len_same += 1
        party_q.append(party_data)
        q_len += 1


print(len(party_q))
# 마지막에 남는 게 무지성 참가자들만의 파티임.