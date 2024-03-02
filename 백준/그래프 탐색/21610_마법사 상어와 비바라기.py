import sys


def moved_cloud(x, y, d, s):
    nx = x + dx[d] * s
    ny = y + dy[d] * s
    while nx < 0:
        nx += N
    while nx > N - 1:
        nx -= N
    while ny < 0:
        ny += N
    while ny > N - 1:
        ny -= N
    return nx, ny


dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
before_cloud = [[False for _ in range(N)] for _ in range(N)]
# 비바라기 시전 후 구름 생성
for i in range(N - 2, N):
    for j in range(0, 2):
        before_cloud[i][j] = True

for num in range(1, M + 1):
    d, s = map(int, input().split())
    after_cloud = [[False for _ in range(N)] for _ in range(N)]
    temp = []
    for i in range(N):
        for j in range(N):
            if before_cloud[i][j]:
                # 1. 모든 구름이 d방향으로 s칸 이동
                ni, nj = moved_cloud(i, j, d, s)
                after_cloud[ni][nj] = True
                temp.append((ni, nj))
                # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양 1 증가
                graph[ni][nj] += 1

    # 4. 2에서 물이 증가한 칸에 물복사 버그 마법 시전
    for i, j in temp:
        for ni, nj in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            if ni < 0 or ni > N - 1 or nj < 0 or nj > N - 1:
                continue
            if graph[ni][nj] > 0 :
                graph[i][j] += 1

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어듦
    before_cloud = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not after_cloud[i][j]:
                graph[i][j] -= 2
                before_cloud[i][j] = True

answer = 0
for i in range(N):
    for j in range(N):
        answer += graph[i][j]

print(answer)