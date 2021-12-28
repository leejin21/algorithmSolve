class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = [-1]
        def binSearch(l, r):
            if l>r: return
            
            m = (r-l)//2 + l
            
            if nums[m] == target:
                answer[0] = m
                return
            elif target < nums[m]:
                binSearch(l, m-1)
            else:
                binSearch(m+1, r)
                
        binSearch(0, len(nums)-1)
        return answer[0]
            
        