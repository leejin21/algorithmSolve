# 1,2,3 더하기

'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

SOLUTION

처음에 아래와 같이 재귀적으로 1,2,3,4... 구해서 배열에 넣어놓기
4 = 1+3
3 = 1+1+1 = 1+2 = 2+1 = 3
2 = 1+1 = 2
1 = 1
'''

import sys; read = sys.stdin.readline

def findWays(n):
    if ways[n] != 0:
        return ways[n]
    tot = 0
    for i in range(1, 4 if n>2 else n+1):
        tot += findWays(n-i)
    ways[n] = tot
    return tot

T = int(read())
ways = [1]*2+[0]*9

for _ in range(T):
    n = int(read())
    findWays(n)
    print(ways[n])


def otherAns():
    def addOneTwoThree(n):
        m = max(n)
        dp = [0 for _ in range(m+1)]
        dp[1]=1; dp[2]=2; dp[3]=4
        for i in range(4,m+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return [dp[i] for i in n]

    for num in addOneTwoThree([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]):
        print(num)