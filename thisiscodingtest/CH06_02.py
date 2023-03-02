# 위에서 아래로
import sys; read = sys.stdin.readline

N = int(read())
nums = [int(read()) for i in range(N)]

print(sorted(nums, reverse=True))
