from collections import defaultdict

class Solution:
    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #     '''
    #     1 ~ n 까지의 사람들 중 타운 저지 자신 빼고 모두 신뢰해야 함
    #     신뢰를 당하는 관계성으로 따지면
    #     타운 저지 -> 1 ~ n, 스스로 제외
        
    #     동시에
        
    #     신뢰를 하는 관계성으로 따지면
    #     타운 저지 -> 아무도 없음.
        
    #     늘 그렇지만, 조건 양 끝단 잘 살피기
        
    #     '''
    #     if n == 1 and len(trust) == 0:
    #         return 1
        
    #     cross_graph = defaultdict(list)
    #     graph = defaultdict(list)
        
    #     for pair in trust:
    #         cross_graph[pair[1]].append(pair[0])
    #         graph[pair[0]].append(pair[1])
            
    #     for k in cross_graph.keys():
    #         if len(cross_graph[k]) == n - 1 and len(graph[k]) == 0:
    #             return k
            
        
    #     return -1
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        신뢰를 하는 것을 -1
        신뢰를 당하는 것을 +1
        로 취급했을 때, n-1만큼의 점수를 가지고 있으면 저지가 됨.
        '''
        if n == 1 and len(trust) == 0:
            return 1
    
        graph = [0]*(n+1)
        
        for pair in trust:
            graph[pair[1]] += 1
            graph[pair[0]] -= 1
            
        for k in range(1, n+1):
            if graph[k] == n - 1:
                return k
            
        return -1
        