# N과 M(4)
import sys; read = sys.stdin.readline
N, M = list(map(int, read()[:-1].split(" ")))
sequences = []


def findSequences(unfinish_seq, prev, depth):
    # print(unfinish_seq, prev, depth)
    if depth == 0:
        sequences.append(unfinish_seq)
    else:
        for i in range(prev, N+1):
            # print(unfinish_seq+[i], depth-1)
            findSequences(unfinish_seq+[i], i, depth-1)

findSequences([], 1, M)
for seq in sequences:
    for i in seq:
        print(i, end=" ")
    print()