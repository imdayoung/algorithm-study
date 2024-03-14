from collections import deque
import sys


def spread():
    spreads = []
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                increase_amount = room[x][y] // 5
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1 or room[nx][ny] == -1:
                        continue
                    spreads.append((nx, ny, increase_amount))
                    room[x][y] -= increase_amount
    for x, y, s in spreads:
        room[x][y] += s


def clean_up():
    queue = deque()
    for j in range(C - 1):
        queue.append(room[0][j])
    for i in range(cleaner_top):
        queue.append(room[i][C - 1])
    for j in range(C - 1, 0, -1):
        queue.append(room[cleaner_top][j])
    queue.append(0)
    for i in range(cleaner_top - 2, 0, -1):
        queue.append(room[i][0])
    queue.append(queue.popleft())

    for j in range(C - 1):
        room[0][j] = queue.popleft()
    for i in range(cleaner_top):
        room[i][C - 1] = queue.popleft()
    for j in range(C - 1, 0, -1):
        room[cleaner_top][j] = queue.popleft()
    for i in range(cleaner_top - 1, 0, -1):
        room[i][0] = queue.popleft()


def clean_down():
    queue = deque()
    for j in range(1, C - 1):
        queue.append(room[cleaner_down][j])
    for i in range(cleaner_down, R - 1):
        queue.append(room[i][C - 1])
    for j in range(C - 1, -1, -1):
        queue.append(room[R - 1][j])
    for i in range(R - 2, cleaner_down + 1, -1):
        queue.append(room[i][0])
    queue.append(0)
    queue.appendleft(queue.pop())

    for j in range(1, C - 1):
        room[cleaner_down][j] = queue.popleft()
    for i in range(cleaner_down, R - 1):
        room[i][C - 1] = queue.popleft()
    for j in range(C - 1, -1, -1):
        room[R - 1][j] = queue.popleft()
    for i in range(R - 2, cleaner_down, -1):
        room[i][0] = queue.popleft()


answer = 0
R, C, T = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기 청정기의 X좌표 구하기
for i in range(R):
    if room[i][0] == -1:
        cleaner_top = i
        cleaner_down = i + 1
        break

for t in range(1, T + 1):
    # 1. 미세먼지 확산
    spread()

    # 2. 공기청정기 작동
    clean_up()
    clean_down()

# T초 후 남아있는 미세먼지의 양 구하기
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            continue
        answer += room[i][j]
        
print(answer)