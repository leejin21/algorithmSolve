import sys; read=sys.stdin.readline

M = int(read())

S = [0]*21

for _ in range(M):
    cmd = read()[:-1].split(" ")
    if cmd[0] == "add":
        S[int(cmd[1])] = 1
    elif cmd[0] == "check":
        print(S[int(cmd[1])])
    elif cmd[0] == "remove":
        S[int(cmd[1])] = 0
    elif cmd[0] == "toggle":
        S[int(cmd[1])] = 0 if S[int(cmd[1])] else 1
    elif cmd[0] == "all":
        for i in range(len(S)):
            S[i] = 1
        
    elif cmd[0] == "empty":
        for i in range(len(S)):
            S[i] = 0
        

    


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