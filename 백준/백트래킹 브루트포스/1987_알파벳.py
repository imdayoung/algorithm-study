import sys


def back_tracking(x, y, cnt):
    global count
    count = max(count, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            continue

        if not visited_alphabet[board[nx][ny]]:
            visited_alphabet[board[nx][ny]] = True
            back_tracking(nx, ny, cnt + 1)
            visited_alphabet[board[nx][ny]] = False


if __name__ == '__main__':
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count = 1

    R, C = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
    visited_alphabet = {chr(i) : False for i in range(ord('A'), ord('Z') + 1)}
    visited_alphabet[board[0][0]] = True

    back_tracking(0, 0, 1)
    print(count)