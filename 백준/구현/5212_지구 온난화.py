import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(R)]
answer = copy.deepcopy(graph)

for x in range(R):
    for y in range(C):
        cnt = 0
        if graph[x][y] == "X":
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1 or graph[nx][ny] == ".":
                    cnt += 1
            if cnt >= 3:
                answer[x][y] = "."

r = len([a[0] for a in answer])
c = len(answer[0])
answer_c = [[a[i] for a in answer] for i in range(c)]

for i in range(r):
    if "X" in answer[i]:
        x_start = i
        break
for i in range(r - 1, -1, -1):
    if "X" in answer[i]:
        x_end = i
        break

for i in range(c):
    if "X" in answer_c[i]:
        y_start = i
        break
for i in range(c - 1, -1, -1):
    if "X" in answer_c[i]:
        y_end = i
        break

for i in range(x_start, x_end + 1):
    for j in range(y_start, y_end + 1):
        print(answer[i][j], end = "")
    print()