# 19M 58S -> 시간 초과
import sys


problems = {i:[] for i in range(1, 100 + 1)}
problems_rev = {}

N = int(sys.stdin.readline())

for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    problems[L].append(P)
    if P not in problems_rev:
        problems_rev[P] = [L]
    else:
        problems_rev[P].append(L)

M = int(sys.stdin.readline())
for _ in range(M):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == 'recommend':
        x = command[1]
        if x == '1':
            for i in range(100, 0, -1):
                if problems[i] != []:
                    print(max(problems[i]))
                    break
        elif x == '-1':
            for i in range(1, 100 + 1):
                if problems[i] != []:
                    print(min(problems[i]))
                    break

    elif command[0] == 'add':
        P = int(command[1])
        L = int(command[2])
        problems[L].append(P)
        if P not in problems_rev:
            problems_rev[P] = [L]
        else:
            problems_rev[P].append(L)

    elif command[0] == 'solved':
        P = int(command[1])
        for level in problems_rev[P]:
            problems[level].remove(P)
        problems_rev.pop(P)
