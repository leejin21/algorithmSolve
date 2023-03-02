def selection_sort(nums):

    for i in range(len(nums)-1):
        # find min num in rest
        min_j = i+1
        for j in range(i, len(nums)):
            if nums[min_j] > nums[j]:
                min_j = j
        
        nums[i], nums[min_j] = nums[min_j], nums[i]

    return nums


print(selection_sort([3,4,5,2,1]))


'''

[선택 정렬]
SELECETION SORT
7 6 5 4 3 2 1
오른쪽 unsorted 구간에서 가장 작은(혹은 큰) 수 골라서 앞으로 데려오기

'''