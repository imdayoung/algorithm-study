# 예제보고 해석하느라 개고생했다 ㅗ
import sys


answer = 0
N, P = map(int, sys.stdin.readline().split())
pressing = [[] for _ in range(6 + 1)]

for _ in range(N):
    line, fret = map(int, sys.stdin.readline().split())

    if pressing[line] and pressing[line][-1] > fret:
        while pressing[line] and pressing[line][-1] > fret:
            pressing[line].pop()
            answer += 1

    if pressing[line] and pressing[line][-1] == fret:
        continue

    pressing[line].append(fret)
    answer += 1

print(answer)