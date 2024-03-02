from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 토마토가 놓여 있는 박스
box = []
# 초기 익은 토마토 위치
tomato = deque()

# 가로 m, 세로 n, 높이 h
m, n, h = map(int, input().split())
# 1 익은 토마토, 0 익지 않은 토마토, -1 토마토가 들어있지 않은 칸
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().rstrip().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                tomato.append([i, j, k])
    box.append(tmp)

while tomato:
    x, y, z = tomato.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx <= -1 or ny <= -1 or nz <= -1 or nx >= h or ny >= n or nz >= m:
            continue
        if box[nx][ny][nz] == -1:
            continue
        if box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            tomato.append([nx, ny, nz])

ans = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans - 1)