# 키패드 누르기


'''

1 2 3
4 5 6
7 8 9
* 0 #

'''

def solution(numbers, hand):
    answer = []; l = (3, 0); r = (3, 2)
    keysd = {0: (3, 1), 1: (0,0), 2: (0,1), 3: (0,2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    for n in numbers:
        y, x = keysd[n]
        if x == 0:
            answer.append('L')
            l = (y, x)
        elif x == 2:
            answer.append('R')
            r = (y, x)
        else:
            if totdiff(y, x, l) < totdiff(y, x, r):
                answer.append('L')
                l = (y, x)
            elif totdiff(y, x, l) == totdiff(y, x, r):
                if hand == 'left': answer.append('L'); l = (y, x)
                else: answer.append('R'); r = (y, x)
            else:
                answer.append('R')
                r = (y, x)
    
    return ''.join(answer)

def totdiff(y, x, u):
    return abs(u[0] - y) + abs(u[1] - x)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))