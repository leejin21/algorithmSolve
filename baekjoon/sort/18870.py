# 좌표 압축

'''
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

SOLUTION

dict() => key.sort() 
keys.sort의 인덱스로.

[2 4 -10 4 -9]
set로 하면-> {2, 4, -9, -10}
keys.sort하면 -> [-10, -9, 4, 2]
dict {-10:0, -9: 1, 4: 2, 2:3}

* 특이점: sorted(list(set(loc_list)))의 위치를 for문 안으로 옮겨줬더니 잘 됨.

'''

import sys; read = sys.stdin.readline

N = read()
loc_list = list(map(int, read()[:-1].split(" ")))

zip_result = dict()

for i, l in enumerate(sorted(list(set(loc_list)))):
    zip_result[l] = i

for l in loc_list:
    print(zip_result[l], end=" ")