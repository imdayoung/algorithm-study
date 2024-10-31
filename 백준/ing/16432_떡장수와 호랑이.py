import sys


def backtracking(day, index, a):
    global found
    global answer

    if found:
        return
    
    if (len(a) == N):
        found = True
        answer = a
        return
    
    for i in range(len(ddeoks[day])):
        if len(a) == 0 or a[-1] != ddeoks[day][i]:
            backtracking(day + 1, i + 1, a + [ddeoks[day][i]])
    

answer = []
found = False
N = int(sys.stdin.readline())
ddeoks = [[]]
for _ in range(N):
    ddeok = list(map(int, sys.stdin.readline().split()))
    ddeoks.append(ddeok[1:])

backtracking(1, 0, [])

if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a)
