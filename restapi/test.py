import requests, json
URL = 'http://www.tistory.com' 

# 기본적인 사용 방법
response = requests.get(URL) 
print(response.status_code, response.text)

# GET 요청할 때 parameter 전달법
params = {'param1': 'value1', 'param2': 'value'}
res = requests.get(URL, params=params)

# POST 요청할 때 parameter 전달법
data = {'param1': 'value1', 'param2': 'value'}
res = requests.post(URL, data=data)


# 헤더 추가, 쿠키 추가
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'session_id': 'sorryidontcare'}
res = requests.get(URL, headers=headers, cookies=cookies)

# 4. 응답(Response) 객체
res.request # 내가 보낸 request 객체에 접근 가능
res.status_code # 응답 코드 
res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
res.json() # json response일 경우 딕셔너리 타입으로 바로 변환

'''

'''
import sys; read = sys.stdin.readline
import collections

sys.setrecursionlimit(10000)

def solution():
    answer = 0
    return answer

N = int(read())
A, K = list(map(int, read()[:-1].split(' ')))
coins = list(map(lambda i: int(read()[:-1]), range(N)))
print(solution())