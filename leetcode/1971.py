from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        여기서 사이클 생기는 경우 고려해야 함: visited 추가하기
        BFS로 진행하기
        '''
        graph = defaultdict(list)
        visited = [False]*n
        
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
    
        q = deque([source])
        
        while(q):
            cur = q.popleft()
            if cur == destination:
                return True
            visited[cur] = True
            for nn in graph[cur]:
                if not visited[nn]:
                    q.append(nn)
        
        return False
            