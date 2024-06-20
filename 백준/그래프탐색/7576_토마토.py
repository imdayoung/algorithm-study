from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

box = []
# 상자의 세로 칸 수 n, 상자의 가로 칸 수 m
m, n = map(int, input().rstrip().split())
# 1 익은 토마토, 0 익지 않은 토마토, -1 토마토가 들어있지 않은 칸
for _ in range(n):
    box.append(list(map(int, input().rstrip().split())))
# 초기 익은 토마토 위치
tomato = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((i, j))

def bfs(tomato):
    queue = deque()
    for t in tomato:
        queue.append((t[0], t[1]))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
        
    # 최종 box 안에 익지 않은 토마토가 있는 지 확인 및 퍼뜨린 횟수 확인
    ans = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
            ans = max(ans, box[i][j])
    return ans - 1

print(bfs(tomato))