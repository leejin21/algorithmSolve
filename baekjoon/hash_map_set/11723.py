import sys; read=sys.stdin.readline

M = int(read())

ans_list = []


def main2():
    S = set()
    for _ in range(M):
        cmd_list = read()[:-1].split(" ")
        cmd = cmd_list[0]
        if len(cmd_list)>1:
            i = int(cmd_list[1]) 
        else: i = None
        isthereans = False; ans = 0
        if cmd == "add":
            S.add(i)
        elif cmd == "check":
            isthereans = True
            if i in S:
                ans = 1
            else:
                ans = 0
        elif cmd == "remove":
            S.discard(i)
        elif cmd == "toggle":
            if i in S:
                S.discard(i)
            else:
                S.add(i)
        elif cmd == "all":
            S = set([i for i in range(1, 21)])
        elif cmd == "empty":
            S = set([])

        if isthereans:
            # ans_list.append(ans)
            print(ans)
        # print(S)

main2()
# print(ans_list)



def main():
    S = [0]*21
    for _ in range(M):
        cmd = read()[:-1].split(" ")
        ans = False
        if cmd[0] == "add":
            S[int(cmd[1])] = 1
        elif cmd[0] == "check":
            ans = S[int(cmd[1])]
        elif cmd[0] == "remove":
            S[int(cmd[1])] = 0
        elif cmd[0] == "toggle":
            S[int(cmd[1])] = 0 if S[int(cmd[1])] else 1
        elif cmd[0] == "all":
            S = [1 for i in range(len(S))]
        elif cmd[0] == "empty":
            S = [0 for i in range(len(S))]

        if ans != False:
            print(ans)


'''
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1




'''