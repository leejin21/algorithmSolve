# 프로그래머스 순위
'''
실력이 같은 경우도 있는 건가 그러면?
'''
import sys; read = sys.stdin.readline

sys.setrecursionlimit(10000)

def solution(n, results):
    # 양방향 그래프 표시 위해 딕셔너리 두개 이용
    visited = {(i+1): False for i in range(n)}
    winGraph = {(i+1):[] for i in range(n)} # 이긴 놈: 진 놈
    loseGraph = {(i+1):[] for i in range(n)} # 진 놈: 이긴 놈
    # graph 형태로 구성
    for result in results:
        winner, loser = result
        winGraph[winner].append(loser)
        loseGraph[loser].append(winner)
    
    def dfs(cur, isWin):
        cnt = 1 # 본인 제외해줘야 함(나중에)
        visited[cur] = True
        graph = winGraph if isWin else loseGraph

        for n in graph[cur]:
            if not visited[n]:
                # 아직 방문하지 않은 노드
                cnt += dfs(n, isWin)
        # print(cur, cnt)
        return cnt
            
    answer = 0
    for curNode in range(1, n+1):
        # visited 초기화
        visited = {(i+1): False for i in range(n)}

        # 현재 노드보다 실력이 떨어지는 노드들 위주
        curNodesLoserCnt = dfs(curNode, True) - 1
        
        # 현재 노드보다 실력이 좋은 노드들 위주
        curNodesWinnerCnt = dfs(curNode, False) - 1

        if curNodesLoserCnt + curNodesWinnerCnt == n-1:
            # 즉 본인에게 지는 놈들 + 본인에게 이기는 놈들이 자신을 제외한 노드의 개수와 일치하는 경우
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))