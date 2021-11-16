# Product of Array Except Self
# [파알인] 11. 자신을 제외한 배열의 곱

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        productList = []
        # left에서부터 곱
        tot = 1
        for i in range(len(nums)):
            productList.append(tot)
            tot *= nums[i]
            
        # right에서부터 곱
        tot = 1
        for j in range(len(nums)-1,-1, -1):
            productList[j] *= tot
            tot *= nums[j]
        
        return productList
        