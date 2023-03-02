# 선택 정렬

def insertion_sort(l):
    for i in range(1, len(l)):  # number to insert
        s_e = i - 1
        for j in range(s_e, -1, -1):    # find the seat
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                i = j
            else:
                break

    return l

print(insertion_sort([7, 6, 5, 4, 3, 2, 1]))
print(insertion_sort([4, 7, 3, 1, 9, 20, 2]))

'''
[삽입 정렬]
INSERTION SORT
7 6 5 4 3 2 1

5 6 7 4 3 2 1
    j i

5 6 4 7 3 2 1
  j i
-> 

cur 기준으로 앞 이미 sorted 구간에서의 자리 찾아주기
'''