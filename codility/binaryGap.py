# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    
    bnum = format(N, 'b')
    answer = 0
    prevOneIdx = 0
    print(bnum)
    for i, n in enumerate(bnum):
        if n == '1':
            if answer < (i - prevOneIdx-1):
                answer = i - prevOneIdx-1
            prevOneIdx = i
        print(i,n,answer)

    return answer


print(solution(1041))