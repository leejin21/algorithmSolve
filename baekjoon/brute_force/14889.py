# 스타트와 링크
'''
문제
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.


i\j	1	2	3	4   5   6
1	 	1	2	3   2   1
2	4	 	5	6   3   4
3	7	1	 	2   1   1
4	3	4	5	    3   2
5   2   3   4   5       2
6   1   2   5   3   2    

선택

TRY 1
스타트 팀과 링크 팀의 중복을 고려하지 못함.
즉 N = 4일 때 스타트={0,1}과 스타트={2,3}이 동일한 결과를 도출한다는 것을 모름

TRY 2
STT는 무조건 0번쨰 사람을 끼고 시작한다고 설정.
그렇게 되면 2nCn / 2= (2n-1)C(n-1) 이므로 중복 없이 구할 수 있음.

stt = {0번째 사람}; link = {}

ak을 stt의 k번째 원소.
a0 = 0
a1 = a0+1 ~ N//2+1번째; a2 = a1+1 ~ N//2+2번째
즉 ak = a(k-1) ~ N//2+k번째까지 가능.
이때 k = 0~ N//2이므로 조건에 만족.

chance = N//2 - k
k = N//2 - chance


예제 입력 3도 1이 안나온다는 게 문제임.
'''
import sys
from collections import deque

stt = deque(); link = deque()

skill = []; N = 0
# root=0
# root는 0 바로 다음에 stt에 들어가는 원소
min_diff = 2147483647

def main():
    global skill, N
    N = int(sys.stdin.readline())
    
    skill = list(map(lambda _: list(map(int, sys.stdin.readline().split())), range(N)))
    drawNew2Teams(0, N//2, 0)
    print(min_diff)

def drawNew2Teams(cur, chance, stt_skill):
    stt_skill += appendNew2Team(stt, cur); chance -= 1
    if chance == 0:
        link_skill = findMissedNewBsLink()
        updateMin(stt_skill, link_skill)
        # print("세트 끝남:", stt, link)
        # print(min_diff, stt_skill, link_skill)
        stt.pop()
        while(len(link)!=0): link.pop()
    else:
        for k in range(cur+1, N-chance+1):
            drawNew2Teams(k, chance, stt_skill)
        stt.pop()
            
def findMissedNewBsLink():
    add_link_ab = 0
    if len(stt) != len(link):
        p = 0
        for i in range(len(stt)):
            add_link_ab += addNewBs2Link(p+1, stt[i])
            # print(p, stt[i], add_link_ab)
            p = stt[i]
        if stt[i]!=N-1: add_link_ab += addNewBs2Link(p+1, N)
        # print(p, stt[i], add_link_ab)
    return add_link_ab

def addNewBs2Link(front, end):
    # print(front, end)
    if front +1 == end:
        return appendNew2Team(link, front)
    else:
        return sum(map(lambda i: appendNew2Team(link, i), range(front, end)))

def appendNew2Team(team, newcomer):
    plus_ability = calcAbility(team, newcomer)
    team.append(newcomer)
    return plus_ability

def calcAbility(team, newcomer):
    global skill
    plus_ability = 0
    for senior in team: 
        plus_ability += skill[newcomer][senior] + skill[senior][newcomer]
    return plus_ability

def updateMin(stt_ability, link_ability):
    global min_diff
    diff = abs(stt_ability - link_ability)
    min_diff = diff if diff<min_diff else min_diff

main()

def try2(cur, chance, stt_ability, link_ability):
    global stt, link, N
    pre_stt_ability = stt_ability; pre_link_ability = link_ability
    print("==============함수 시작================")
    stt_ability += appendNew2Team(stt, cur)
    chance -= 1
    if chance == 0: 
        # 해당 세트는 끝남
        link_ability += findMissedNewBsLink()
        updateMin(stt_ability, link_ability)
        if cur==N-1: 
            # a1=root인 모든 세트 종료
            print(root, "인 모든 세트 종료")
            print(0, root, cur)
            print('chance = ', chance, stt, link)
            # return
        else: 
            # a1=root인 세트 덜 끝남
            print(root, "인 어떤 세트 종료")
            print(0, root, cur)
            print('chance = ', chance, stt, link)
            stt.pop()
            while(len(link)!=0): link.pop()
            try2(cur+1, chance+1, pre_stt_ability, pre_link_ability)
    elif chance > 0:
        # 해당 세트 아직 덜 끝남.
        print(root, "인 어떤 세트 미종료")
        print(0, root, cur)
        print('chance = ', chance, stt, link)
        # TODO 여기가 문제! 왜 더럽게 남겨질까? 어떻게 하면 덜 더럽게 남겨질까?
        print('for문 시작')
        # for next in range(cur+1, N-chance+1):
        #     drawNew2Teams(next, chance, stt_ability, link_ability)
        try2(cur+1, chance, stt_ability, link_ability)
        print("for문 끝", 0, root, cur)

# try1
def drawNew2Teams2(cur, depth, stt_ability, link_ability):
    # 편의상 root부터 depth = 1로 취급.
    global stt, link, N
    stt_ability += appendNew2Team(stt, cur)
    print('root=', root,', cur, depth =', cur, depth)
    print(stt, link)
    if root == N/2 and depth == N/2: # 모든 세트 완전히 종료        
        return
    elif depth != N/2: # 세트 아직 덜 끝남.
        for next in range(cur+1, N):
            if cur+1 != next: link_ability += addNewBs2Link(cur+1, next)
                # link에 추가
            drawNew2Teams2(next, depth+1, stt_ability, link_ability)
    else:
        # N/2개 다 뽑았고 다음으로 넘어가기 직전.
        if cur+1 != N: link_ability += addNewBs2Link(cur+1, N)
            # 직전 뽑은 것+1~ 마지막까지 link에 추가
        if len(stt) != len(link):
            # 오류 걸러내기
            print("오류:", len(stt), len(link), N/2); return
        else: updateMin(stt_ability, link_ability)
        print('마무리')
        print('root=', root,', cur, depth =', cur, depth)
        print(stt, link)
        
        initValues2()
        print('초기화')
        
        link_ability = addNewBs2Link(0, root)
        print(root, stt, link)
        drawNew2Teams(root, 1, 0, link_ability)
            # root 업글해서 다시 시작: 이제 root...N-1까지만 고려해서 뽑는 세트

def initValues2():
    # 해당 세트 끝나고 다음 세트 준비
    global root, stt, link
    root+= 1; stt = deque(); link = deque()
    stt_ability = 0; link_abilty = 0

