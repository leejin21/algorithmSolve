# [1차] 다트 게임

'''
1S2D*3T

S, D, T로 끊되 바로 뒤에 * 나 # 이 들어오면 그렇게 문자열 끊어주기.

1S 2D* 3T

'''

def solution(dartResult):
    answer = 0; front = 0; pre = 0
    exponents = {'S': 1, 'D': 2 ,'T': 3}

    for end in range(1, len(dartResult) if dartResult[-1] in ['*', '#'] else len(dartResult)+1):
        if dartResult[end-1] in ['S', 'D', 'T']:
            temp = pow(int(dartResult[front:end-1]), exponents[dartResult[end-1]])
            if end < len(dartResult):
                front = end + 1
                if dartResult[end] == '*':
                    temp *= 2
                    answer += pre
                elif dartResult[end] == '#': 
                    temp *= -1
                else: front = end
            answer += temp
            pre = temp
    
    return answer

solution('1S2D*3T')
solution('1D2S#10S')
solution('1D2S0T')
solution('1S*2T*3S')
solution('1D#2S*3S')
solution('1T2D3D#')
solution('1D2S3T*')

