# while문으로 이진 탐색 구현하기

def binarySearch(item, stt, end):
    ans = -1

    while(stt <= end):
        mid = stt + (end - stt)//2
        if l[mid] == item:
            ans = mid
            break
        elif l[mid] < item:
            stt = mid + 1
        else:
            end = mid - 1

    return ans

l = [1,2,3,4,5,6]
ans = binarySearch(1, 0, len(l)-1)
print(ans)


'''
mid 기준

while문 -> stt <= end일 경우

item == l[mid]
    해당 인덱스
l[mid] < item
    오른쪽 ㄱ
l[mid] > item
    왼쪽 ㄱ

'''