'''
문제 설명

하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.
예를들어
- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청


이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.
각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
- jobs의 길이는 1 이상 500 이하입니다.
- jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
- 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
- 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
- "하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다."

[0, 3] => 3-0 (3)
[1, 9] => 3>1: 3+9 (10)
[2, 6] => (8)

: 그리디처럼, 일단 3초 후에 남은 작업들 중 가장 빨리 끝나는 애 데려올까..

우선순위 큐에서 어떤 게 우선순위로 고려되어야 할까?


prev_last = last_end
last_end = 


* 여러 가지 경우 생각하기 *
1. [0, 10], [2, 10], [9, 10], [15, 2] 의 경우에 [15, 2]를 


'''
import heapq

first_le = 0
tot = 0; last_end = 0

def solution(jobs):
    global first_le, tot, last_end
    
    i = 0; heap = []
    while (i<len(jobs)):
        print("job: ", jobs[i])
        if jobs[i][0] >= last_end:
            # 하드디스크가 작업을 수행하고 있지 않는 경우
            while(len(heap) != 0):
                popJob(heap, jobs)
                if jobs[i][0] < last_end: break
            
            if jobs[i][0] >= last_end:
                # 위 while문에 의해 갱신된 last_end에 대해서 job의 수행 시작 시간이 더 뒤에 있는지
                # 즉, 하드 디스크가 놀고 있는지
                tot += jobs[i][1]
                last_end = jobs[i][1] + jobs[i][0]
                print(" heap:", heap, "tot:", tot, "last_end", last_end)
            else:
                    # 위 while문에 의해 갱신된 last_end에 대해서 job의 수행 시작 시간이 더 앞에 있는지
                    # 즉, 바로 직전 작업을 하드 디스크가 하는 도중에 job이 들어왔을 때
                pushJob(heap, jobs, i)
        else:
            # 하드디스크가 작업을 수행하고 있는 경우
            pushJob(heap, jobs, i)
        i+=1
    while(len(heap)!=0): popJob(heap, jobs)
    # return tot
    return tot//len(jobs)

def pushJob(heap, jobs, i):
    global first_le, tot, last_end
    heapq.heappush(heap, (last_end+jobs[i][1], jobs[i][0], last_end))
    # first_le = last_end
    print(" heap:", heap, "tot:", tot, "last_end", last_end)

def popJob(heap, jobs):
    # heap에 있는 애들 다 빼서 tot에 합해 주기(하드디스크가 작업하는 도중에 요청 들어오는 게 끝남)
    global first_le, tot, last_end
    predt, stt, fend = heapq.heappop(heap)
    perft = predt - fend; waitt = last_end - stt
    tot += perft + waitt
    last_end += perft
    print("waitt: ", waitt)
    print(" heap:", heap, "tot:", tot, "last_end", last_end)

# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[0, 100], [75, 50], [96, 10], [160, 30]]))
# print(solution([[0, 20], [3, 4], [3, 5], [17, 2]]))
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))