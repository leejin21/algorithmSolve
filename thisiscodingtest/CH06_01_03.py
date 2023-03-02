
# should reprogram it
def quick_sort(s, e):
    pivot = l[s]

    i = s+1; j = e
    while(i<=j):
        if (i<=e or j>=0):
            break

        if (l[i] <= pivot){
            i+=1
        }
        if (l[j] > pivot){
            j-= 1
        }
        
        if (l[i] > pivot and l[j] <= pivot){
            l[i], l[j] = l[j], l[i]
        }

    # swap pivot and middle
    l[s], l[i] = l[i], l[s]

    quick_sort(s, i-1)
    quick_sort(i+1, e)


l = [7, 5, 9]
quick_sort(0, len(l)-1)

'''
[퀵 정렬]
7 6 5 4 3 2 1

1. 가장 왼쪽 pivot(s) 잡고
s+1에서 시작하는 i, e에서 시작하는 j
pivot < 값i , pivot > 값j 인 i, j 찾고 서로 swap
이때 i>j이 되는 순간: s랑 i swap 해주기(당연히 작은 거랑 변경해주기!)

2. 분할

pivot 기준으로 왼쪽, 오른쪽 분리 후 각각에 대해 퀵 소트 진행

'''