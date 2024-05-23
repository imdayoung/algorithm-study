import sys


answer = 0

N = int(sys.stdin.readline())
current = list(map(int,sys.stdin.readline().rstrip()))
target = list(map(int, sys.stdin.readline().rstrip()))

for i in range(N):
    print(current)
    if current[i] != target[i]:
        answer += 1
        switch = (current[i] + 1) % 2
        
        current[i] = switch
        if i - 1 > -1:
            current[i - 1] = switch
        if i + 1 < N:
            current[i + 1]
        
if current == target:
    print(answer)
else:
    print(-1)
