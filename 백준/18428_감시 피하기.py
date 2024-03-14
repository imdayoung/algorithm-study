import sys


def build_obstacle(cnt):
    global answer
    if cnt == 3:
        if is_avoidable():
            answer = "YES"
        return
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                build_obstacle(cnt + 1)
                graph[i][j] = 'X'
            if answer == "YES":
                return


def is_avoidable():
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 'T':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] == 'O':
                            break
                        if graph[nx][ny] == 'S':
                            return False
                        nx += dx[i]
                        ny += dy[i]
    return True


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

answer = "NO"

N = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(N)]
build_obstacle(0)
print(answer)