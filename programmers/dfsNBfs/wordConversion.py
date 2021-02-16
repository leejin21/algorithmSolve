'''
PROBLEM

두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.
두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.


입출력 예
begin	target	words	return
hit	cog	[hot, dot, dog, lot, log, cog]	4
hit	cog	[hot, dot, dog, lot, log]	0

'''

'''
SOLUTION

dfs로 풀기, O(c*n^2)
c는 단어의 길이, 10이하의 상수

'''

def solution(begin, target, words):
    # dfs: stack 이용

    # * 변수들 초기화
    stack = []; min_cnt = 100
    try:
        target_pos = words.index(target)
    except:
        return 0
    stack.append([begin, -1, 0])
    
    # * dfs, 가지치기 있음.
    while(stack):
        cur, cur_pos, cnt = stack.pop()
        # 차례로 단어, words에서 단어의 인덱스 위치, 현재까지 루트에서 변환한 cnt 개수
        if cur_pos == target_pos and min_cnt > cnt:
            # 종결 조건
            min_cnt = cnt
        for i, w in enumerate(words):
            if diffAlp(cur, w) == 1 and min_cnt>cnt+1:
                # 한글자만 차이나고 최소 변환 cnt보다 cnt+1(다음 cur가 target일 수 있음)가 작은 지
                # 두번째 조건은 가지치기 조건
                stack.append([w, i, cnt+1])
        
    return min_cnt

def diffAlp(w1, w2):
    # * 단어 두개를 받아서 다른 알파벳의 개수 리턴해주기
    # O(단어의 길이), 단어의 길이=상수<10
    cnt = 0
    for a, b in zip(w1, w2):
        if a != b:
            cnt += 1
    return cnt


print(solution("hit", "cog", ["hot", "dot", 'dog', 'lot', 'log', 'cog']))
print(solution("hit", "cog", ["hot", "dot", 'dog', 'lot', 'log']))
# print(getDiffAlpList(["hot", "dot", 'dog', 'lot', 'log', 'cog']))