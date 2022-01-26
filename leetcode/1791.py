class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''
        무방향 그래프
        모든 edges에 들어 있는 노드 번호로 출력해여 함
        '''
        graph = [0]*(len(edges)+2)
        for pair in edges:
            n1, n2 = pair
            graph[n1] += 1
            graph[n2] += 1
        
        for i in range(1, len(edges)+2):
            if graph[i] == len(edges):
                return i
            