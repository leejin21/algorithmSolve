# 재귀로 이진 탐색 구현하기

def binarySearch(item, stt, end):
    if stt > end:
        # when searching item not found
        return -1
    mid = stt + (end - stt)//2
    if l[mid] == item:
        return mid
    elif l[mid] > item:
        return binarySearch(item, stt, mid-1)
    else:
        return binarySearch(item, mid+1, end)


l = [2,3,4,5,6,7]
idx = binarySearch(5, 0, len(l)-1)
print(idx)

'''
item: search하고자 하는 숫자

l[mid] == item: 
    return mid
l[mid] > item:
    왼쪽 탐색
l[mid] < item: 
    오른쪽 탐색
'''