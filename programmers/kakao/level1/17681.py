def solution(n, arr1, arr2):
    answer = []
    for r1, r2 in zip(arr1, arr2):
        # print("%05d"%int(str(bin(r1)[2:])), "%05d"%int(str(bin(r2)[2:])))
        answer.append(list(map(lambda x: '#' if int(x[0]) or int(x[1]) else ' ', zip(putZero(n, str(bin(r1)[2:])), putZero(n, str(bin(r2)[2:]))))))
    # print(answer)
    return list(map(lambda i: ''.join(i), answer))

def putZero(n, st_num):
    return '0'*(n - len(st_num)) + st_num

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

