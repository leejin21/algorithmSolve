# 듣보잡

'''
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

# set으로 또 풀어 보기

'''
# defaultdict로 푼 결과
import sys
from collections import defaultdict

N, M = tuple(map(int, sys.stdin.readline()[:-1].split()))
listenx = list(map(lambda _: (sys.stdin.readline()[:-1], 1), range(N)))
seex = list(map(lambda _: sys.stdin.readline()[:-1], range(M)))

union = defaultdict(int, listenx)
ans = []
for name in seex:
    if union[name] == 1:
        ans.append(name)

ans.sort()
print(len(ans))
for a in ans:
    print(a)