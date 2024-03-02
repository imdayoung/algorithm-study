from collections import deque
import sys


time = 0

# 방향 정보
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

# 뱀의 초기 위치 설정
snake = deque([(0, 0)])
x_head, y_head = 0, 0

# 보드 생성
N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과의 위치 저장
K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1

# 방향 변환 정보 저장
rotates_idx = 0
rotates = []
L = int(sys.stdin.readline())
for _ in range(L):
    temp = sys.stdin.readline().split()
    rotates.append((int(temp[0]), temp[1]))

while True:
    # 몸길이를 늘려 머리를 다음칸에 위치
    x_head += directions[direction][0]
    y_head += directions[direction][1]

    # 벽이나 자기 자신의 몸과 부딪히면 게임 끝
    if x_head < 0 or x_head > N - 1 or y_head < 0 or y_head > N - 1 or (x_head, y_head) in snake:
        break

    snake.append((x_head, y_head))

    #이동한 칸에 사과가 있는 경우 사과가 없어지고 꼬리는 움직이지 않음
    if board[x_head][y_head] == 1:
        board[x_head][y_head] = 0

    # 이동한 칸에 사과가 없는 경우 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
    else:
        snake.popleft()

    time += 1

    # 방향 회전
    if rotates_idx <= L - 1:
        if time == rotates[rotates_idx][0]:
            if rotates[rotates_idx][1] == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
            rotates_idx += 1
    
print(time + 1)