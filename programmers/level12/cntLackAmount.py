# 부족한 금액 계산하기

'''
price * cnt(cnt+1)//2 - money

음수면: 0
양수면: 그대로 return


'''

def solution(price, money, count):
    
    answer = price*count*(count+1)//2 - money
    answer = answer if answer > 0 else 0

    return answer