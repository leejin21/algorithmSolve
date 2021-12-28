
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = 0
        def binSearch(l, r):
            nonlocal answer
            # print(l, r)
            m = (r-l)//2 + l
            # median
            
            if l>r: 
                answer = l
                return
            
            if nums[m] == target:
                answer = m
            elif target < nums[m]:
                binSearch(l, m-1)
            else:
                binSearch(m+1, r)
        
        binSearch(0, len(nums)-1)
        return answer