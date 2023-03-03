# 시간 측정하기 : 100만개짜리 배열 sort

import time

def main():
    array = [i for i in range(12000001, 1, -3)]
    array.sort()

start_time = time.time()
main()

print("-----%s seconds ---" % (time.time() - start_time))

