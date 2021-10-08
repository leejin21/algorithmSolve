'''
입출력 예
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''


def solution(numbers, hand):
    answer = []
    keypad2 = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
                0: (3,1)
    }
    left_hand = (3,0); right_hand = (3,2)
    cur_hand = 'L'
    for num in numbers:
        # num에 따른 손 append하기
        if keypad2[num][1] == 0:
            # 왼쪽 손
            cur_hand = 'L'
        elif keypad2[num][1] == 2:
            # 오른쪽 손
            cur_hand = 'R'
        else:
            # 거리 구하기
            left_dist = abs(keypad2[num][1] - left_hand[1]) + abs(keypad2[num][0]- left_hand[0])
            right_dist = abs(keypad2[num][1] - right_hand[1]) + abs(keypad2[num][0]- right_hand[0])
            # 거리에 따라 손 결정
            if left_dist < right_dist:
                cur_hand = 'L'
            elif left_dist > right_dist:
                cur_hand = 'R'
            else:
                # 거리가 같으면 선호 손으로 정하기
                if hand == 'left':
                    cur_hand = 'L'
                else:
                    cur_hand = 'R'
            
        # 정한 손에 좌표 업데이트
        if cur_hand == 'L':
            left_hand = keypad2[num]
        else:
            right_hand = keypad2[num]
        
        # 정한 손 answer 배열에 추가
        answer.append(cur_hand)
    return ''.join(answer)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))