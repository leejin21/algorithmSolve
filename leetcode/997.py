from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        1 ~ n 까지의 사람들 중 타운 저지 자신 빼고 모두 신뢰해야 함
        신뢰를 당하는 관계성으로 따지면
        타운 저지 -> 1 ~ n, 스스로 제외
        
        동시에
        
        신뢰를 하는 관계성으로 따지면
        타운 저지 -> 아무도 없음.
        
        늘 그렇지만, 조건 양 끝단 잘 살피기
        
        '''
        if n == 1 and len(trust) == 0:
            return 1
        
        cross_graph = defaultdict(list)
        graph = defaultdict(list)
        
        for pair in trust:
            cross_graph[pair[1]].append(pair[0])
            graph[pair[0]].append(pair[1])
            
        for k in cross_graph.keys():
            if len(cross_graph[k]) == n - 1 and len(graph[k]) == 0:
                return k
            
        
        return -1
        