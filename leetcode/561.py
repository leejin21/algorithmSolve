# Array Partition 1
# [파알인] 10. 배열 파티션
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
            1. 정렬
            2. 짝수번째 인덱스를 더해줌

            다른 방법으로 인덱싱 사용하는 경우 있음!
        '''
        sorted_nums = sorted(nums)
        return sum([n for i,n in enumerate(sorted_nums) if i%2==0])
        