import sys


RYAN, APEACH = 1, 2

N, K = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))

answer = N + 1
start, end = 0, 0
ryan = 1 if dolls[end] == RYAN else 0

while end != N:
    if ryan == K:
        answer = min(answer, end - start + 1)
        if dolls[start] == RYAN:
            ryan -= 1
        start += 1
    else:
        end += 1
        if end == N:
            break
        if dolls[end] == RYAN:
            ryan += 1

if answer == N + 1:
    print(-1)
else:
    print(answer)