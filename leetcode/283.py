# O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 160ms 소비
        '''
        0 1 0 3 12
        1 1 0 3 12
        1 3 0 3 12
        1 3 12 3 12
        
        1 3 12 0 0
        '''
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        
        for k in range(i, len(nums)):
            nums[k] = 0
        
        
        
        # 5444ms 소비
        '''
        '0 "1 0 3 12
        1 '0 0 "3 12
        1 3 '0 0 "12
        1 3 12 '0 0 "
        
        p1 = <0 시작 포인터>, p2 = <0 뒤의 숫자 중 시작 포인터>
        이때 swap해 주기
        p2은 제자리 찾아가고(0 아닌 값 찾을 떄까지 +1),
        -> p2이 len(nums)와 같아질 때(즉, upper bound보다 높은 데에 도달했을 때) 종료
        p1도 제자리 찾아감(0인 값 찾을 떄까지 +1),
        '''
        
#         p1 = 0; p2 = 0
        
#         while(p2 < len(nums) and p1 < len(nums)):
#             # print(nums)
            
#             if nums[p1] == 0:
#                 p2 = p1
#                 while(p2 < len(nums) and nums[p2]==0):
#                     p2 += 1
#                 if p2 < len(nums) and nums[p1] == 0 and nums[p2] != 0:
#                     # 적절한 p1, p2일 경우: swap
#                     nums[p1], nums[p2] = nums[p2], nums[p1]
#             else:
#                 # 첫번째 0 찾을 때까지 인덱스 증가
#                 p1 += 1
            
        # print(nums)
            