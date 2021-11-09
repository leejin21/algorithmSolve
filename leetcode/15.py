# 3Sum
# [파알인] #09 세 수의 합

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                # 중복 방지
                continue
            
            left = i+1; right = len(nums)-1
            while(left<right):
                sum = nums[i]+nums[left]+nums[right]
                if sum > 0:
                    right -= 1                    
                elif sum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    while(left<right and nums[left] == nums[left+1]):
                        # left 중복방지
                        left += 1
                    while(left<right and nums[right] == nums[right-1]):
                        # right 중복방지
                        right-= 1
                            
                    left +=1; right -= 1
        return answer