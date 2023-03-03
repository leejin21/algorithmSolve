# CH07 02. 부품 찾기
import time
import sys; read = sys.stdin.readline

def binarySearch(l, item, stt, end):
    if stt > end:
        return -1
    
    mid = stt + (end - stt)//2
    if l[mid] == item:
        return mid
    elif l[mid] < item: # 오른쪽 ㄱ
        return binarySearch(l, item, mid+1, end)
    else: # 왼쪽 ㄱ
        return binarySearch(l, item, stt, mid-1)

def main(part_list, want_list):
    ans_list = []
    part_list.sort()

    for want in want_list:
        ans = binarySearch(part_list, want, 0, len(part_list)-1)
        if ans == -1:
            ans_list.append('no')
        else:
            ans_list.append('yes')

    return ans_list

N = int(read().rstrip())
part_list = [int(i) for i in read().rstrip().split(' ')]

M = int(read().rstrip())
want_list = [int(i) for i in read().rstrip().split(' ')]

stt_time = time.time()
print(main(part_list, want_list))

print('------ %s time spend ------'%(time.time()- stt_time))

'''


5
8 3 7 9 2
3
5 7 9

'''