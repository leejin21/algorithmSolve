# trapping_rain_water
# [파알인] #08 빗물 트래핑

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0; right = len(height) - 1; volume = 0
        left_max = height[left]; right_max = height[right]
        while(left<right):
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if (left_max <= right_max):
                volume += left_max - height[left]
                left += 1
            elif(left_max > right_max):
                volume += right_max - height[right]
                right -= 1
        
        return volume
        