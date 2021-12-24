class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(tot: int, idx:int, temp: List[int]):
            # print(tot, idx, temp)
            if tot == 0:
                answer.append(temp)
                return
            if tot < 0:
                return
            
            for i in range(idx, len(candidates)):
                dfs(tot-candidates[i], i, temp+[candidates[i]])
        
        for i in range(len(candidates)):
            dfs(target-candidates[i], i, [candidates[i]])
        return answer