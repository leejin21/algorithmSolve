# 별 찍기 - 10

'''
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.

1차 시도
하나하나 내려가서 하려고 했는데, 접근이 틀렸다는 것을 알아챘다.

2차 시도
i_stt, i_end, j_stt, j_end


'''
import sys; read = sys.stdin.readline

basic = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

def getPattern(n):
    global star_pattern
    if n == 3:
        # 종결 조건
        # 어디에 append를 해 줘야 할 지 고민해야 함.
        return basic
    else:
        unit = getPattern(n//3)
        pattern = []
        pattern.extend(list(map(lambda _: [], range(n))))
        for i in range(3):
            for j in range(3):
                
                if i == 1 and j == 1:
                    # 현재 
                    for ri in range(i*n//3, (i+1)*n//3):
                        pattern[ri].extend([' ']*(n//3))
                else:
                    for x in range(n//3):
                        pattern[x+i*n//3].extend(unit[x])
                
            
        return pattern
                    
        
def print_pattern(star_pattern):
    for p in star_pattern:
        print(''.join(p))
            
        

N = int(read())
star_pattern = list(map(lambda _: [], range(N)))
# getPattern(N)
print_pattern(getPattern(N))

# 행 미리 만들어주기