import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        trace = [False]*100000
        visit = [False]*100000
        graph = collections.defaultdict(list)
        
        def checkIfCycle(cur: int) -> bool:
            if trace[cur]: return False
            if visit[cur]: return True
            
            trace[cur] = True
            
            for i in list(graph[cur]):
                answer = checkIfCycle(i)
                if not answer:
                    return False
                
            trace[cur] = False
            visit[cur] = True
            
            return True
            
        
        for a, b in prerequisites:
            # b를 끝내야 a를 시작할 수 있음.
            graph[a].append(b)
        
        for k in list(graph.keys()):
            if not checkIfCycle(k): return False
        
        return True