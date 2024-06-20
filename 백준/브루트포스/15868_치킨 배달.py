import sys
input = sys.stdin.readline


def back_tracking(start):
    global answer
    if len(arr) == M:
        temp = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    dist = int(1e9)
                    for a in arr:
                        dist = min(dist, abs(i - a[0]) + abs(j - a[1]))
                    temp += dist
        answer = min(answer, temp)
        return

    for i in range(start, k):
        arr.append(chickens[i])
        back_tracking(i + 1)
        arr.pop()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = int(1e9)
N, M = map(int, input().split())
board = []
chickens = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            chickens.append((i, j))
    board.append(temp)

arr = []
k = len(chickens)
back_tracking(0)
print(answer)