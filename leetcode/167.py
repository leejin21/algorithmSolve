class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointer 
        '''
        문제 조건 자체가 0,0 은 되는데 0 자체로는 안된다는 것인 듯.
        
        '''
        # 해시맵 사용1, 56ms
        hashmap = dict()
        for i in range(len(numbers)):
            n = numbers[i]
            if target - n in hashmap:
                return [hashmap[target-n]+1, i+1]
            else:
                hashmap[n] = i
        
        
        
        # 투 포인터 사용, 91ms
        # i, j = 0, len(numbers)-1
        # while(i<j):
        #     tot = numbers[i]+numbers[j]
        #     if tot == target:
        #         return [i+1, j+1]
        #     elif tot > target:
        #         j -= 1
        #     else:
        #         i += 1
        
        
        # 해시맵 사용2, 105ms
#         hashmap = dict()
#         for i in range(len(numbers)):
#             hashmap[numbers[i]] = i
        
#         for i in range(len(numbers)):
#             if target - numbers[i] in hashmap and hashmap[target - numbers[i]] != i:
#                 return [i+1, 1+hashmap[target - numbers[i]]]
        