import sys
input = sys.stdin.readline

# 인접한 칸 중 좋아하는 학생이 있는 칸과 비어있는 칸의 개수 반환
def check_adjacent(x, y, std):
    count_favorite = 0
    count_empty = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
            continue
        if seats[nx][ny] in favorites[std]:
            count_favorite += 1
        elif seats[nx][ny] == 0:
            count_empty += 1

    return count_favorite, count_empty

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
seats = [[0] * N for _ in range(N)]
favorites = [[] for _ in range(N ** 2 + 1)]
stduents = []

for _ in range(N ** 2):
    like = list(map(int, input().split()))
    stduents.append(like[0])
    favorites[like[0]] = like[1:]

for student in stduents:
    position_x, position_y = 0, 0
    max_favorite, max_empty = 0, 0
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if seats[i][j] != 0:
                continue
            
            f, e = check_adjacent(i, j, student)
            if f > max_favorite:
                position_x, position_y = i, j
                max_favorite = f
                max_empty = e

            elif f == max_favorite:
                if e >= max_empty:
                    position_x, position_y = i, j
                    max_favorite = f
                    max_empty = e

    seats[position_x][position_y] = student

answer = 0
for i in range(N):
    for j in range(N):
        f, e = check_adjacent(i, j, seats[i][j])
        if f == 0:
            answer += 0
        else:
            answer += 10 ** (f - 1)

print(answer)